#!/usr/bin/env python3
"""LearningHub public documentation checks. Offline, deterministic and read-only."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml

REQUIRED = ("id", "title", "version", "status", "classification", "created_at", "updated_at")
STATES = {"draft", "in-review", "approved", "superseded"}

# Exact sizes of the public canonical tables, NOT counts of source documents.
# Update only with an explicit documentary review and matching test changes.
REGISTRIES = (
    ("docs/00-context/04-open-questions.md", "LH-OPEN", 3, 12),
    ("docs/00-context/03-decisions-register.md", "LH-DEC", 3, 8),
    ("docs/07-architecture/05-adr-register.md", "LH-ADR", 3, 10),
    ("docs/05-mvp/01-user-journeys.md", "LH-UJ", 2, 9),
    ("docs/03-requirements/00-functional-requirements.md", "LH-FR", 3, 10),
)

def frontmatter(text: str) -> dict | None:
    m = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", text, re.S)
    if m is None:
        return None
    obj = yaml.safe_load(m.group(1))
    if not isinstance(obj, dict):
        raise ValueError("frontmatter YAML non mapping")
    return obj


def check_metadata(root: Path) -> list[str]:
    errors = []
    ids: dict[str, str] = {}
    for file in sorted((root / "docs").rglob("*.md")):
        rel = file.relative_to(root).as_posix()
        try:
            fm = frontmatter(file.read_text(encoding="utf-8"))
        except (UnicodeError, yaml.YAMLError, ValueError) as exc:
            errors.append(f"{rel}: frontmatter invalide ({type(exc).__name__})")
            continue
        if fm is None:
            errors.append(f"{rel}: frontmatter manquant")
            continue
        for name in REQUIRED:
            if name not in fm or fm[name] in (None, "", []):
                errors.append(f"{rel}: champ requis manquant {name}")
        doc_id = fm.get("id")
        if isinstance(doc_id, str) and doc_id.strip():
            if doc_id in ids:
                errors.append(f"{rel}: id duplique {doc_id} (aussi dans {ids[doc_id]})")
            ids[doc_id] = rel
        elif doc_id is not None:
            errors.append(f"{rel}: id doit etre une chaine non vide")
        if fm.get("classification") != "public":
            errors.append(f"{rel}: classification non publique")
        status = fm.get("status")
        if status not in STATES:
            errors.append(f"{rel}: statut hors cycle public")
        for field in ("created_at", "updated_at"):
            value = fm.get(field)
            if isinstance(value, datetime):
                errors.append(f"{rel}: {field} doit etre YYYY-MM-DD")
            elif isinstance(value, date):
                continue
            elif not (isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)):
                errors.append(f"{rel}: {field} invalide")
            else:
                try:
                    date.fromisoformat(value)
                except ValueError:
                    errors.append(f"{rel}: {field} invalide")
    return errors


def check_registries(root: Path) -> list[str]:
    """Validate only canonical ID rows of the owning tables.

    Mentions in prose and source ranges such as BF-LH-001..004 are not rows.
    """
    errors: list[str] = []
    for name, prefix, width, maximum in REGISTRIES:
        file = root / name
        if not file.is_file():
            errors.append(f"{name}: registre absent")
            continue
        pattern = re.compile(rf"{re.escape(prefix)}-(\d{{{width}}})")
        ids: list[int] = []
        for line in file.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            first_cell = line.split("|", 2)[1].strip().strip("`")
            m = pattern.fullmatch(first_cell)
            if m:
                ids.append(int(m.group(1)))
        count = Counter(ids)
        duplicates = sorted(n for n, amount in count.items() if amount > 1)
        missing = sorted(set(range(1, maximum + 1)) - set(ids))
        extra = sorted(set(ids) - set(range(1, maximum + 1)))
        if missing or duplicates or extra:
            errors.append(f"{name}: {prefix} manque={missing} doublons={duplicates} hors_plage={extra}")
    return errors

class _HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value and ((tag == "a" and key == "href") or (tag in ("img", "source") and key == "src")):
                self.links.append(value)

    handle_startendtag = handle_starttag


def _targets(md: MarkdownIt, content: str) -> list[str]:
    targets: list[str] = []
    for token in md.parse(content):
        candidates = [token] + (token.children or [])
        for child in candidates:
            if child.type == "link_open":
                targets.append(child.attrGet("href") or "")
            elif child.type == "image":
                targets.append(child.attrGet("src") or "")
            elif child.type in ("html_block", "html_inline"):
                html = _HTMLLinks()
                html.feed(child.content)
                targets.extend(html.links)
    return targets


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    files = ([root / "README.md"] if (root / "README.md").is_file() else []) + list((root / "docs").rglob("*.md"))
    for file in sorted(files):
        rel = file.relative_to(root).as_posix()
        try:
            urls = _targets(md, file.read_text(encoding="utf-8"))
        except (UnicodeError, ValueError) as exc:
            errors.append(f"{rel}: Markdown illisible ({type(exc).__name__})")
            continue
        for url in urls:
            if not url or url.startswith(("#", "//")):
                continue
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue  # No external requests, no external URL validation.
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith("/"):
                errors.append(f"{rel}: lien local absolu interdit ({path})")
                continue
            target = (file.parent / path).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{rel}: lien hors depot ({path})")
                continue
            if not target.exists():
                errors.append(f"{rel}: cible absente ou casse incorrecte ({path})")
    return errors


def validate(root: Path) -> list[str]:
    if not (root / "docs").is_dir():
        return ["docs/: dossier manquant"]
    return check_metadata(root) + check_registries(root) + check_links(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict", action="store_true", help="exit 1 on any validation error")
    args = parser.parse_args()
    issues = validate(args.root.resolve())
    for item in issues:
        print("ERROR:", item, file=sys.stderr)
    print(f"Documentation Quality: {len(issues)} anomalie(s)")
    return int(bool(issues) and args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
