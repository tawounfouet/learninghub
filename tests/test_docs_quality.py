"""Positive and negative synthetic fixtures for LearningHub documentation CI."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import docs_quality as dq


def metadata(doc_id: str, *, status: str = "draft",
             classification: str = "public",
             updated_at: str = "2026-11-24") -> str:
    return (
        "---\n"
        f"id: {doc_id}\n"
        'title: "Documentation fixture"\n'
        'version: "0.1.0"\n'
        f"status: {status}\n"
        f"classification: {classification}\n"
        'created_at: "2026-11-24"\n'
        f'updated_at: "{updated_at}"\n'
        "---\n\n# Fixture\n"
    )


class TestDocsQuality(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.write("README.md", "[Docs](docs/README.md)\n")
        self.write("docs/README.md", metadata("LH-FIX-INDEX"))
        self.write("docs/example.md", metadata("LH-FIX-001"))
        for i, (path, prefix, width, count) in enumerate(dq.REGISTRIES):
            rows = "| ID | Description |\n|---|---|\n"
            rows += "".join(f"| `{prefix}-{n:0{width}d}` | Synthétique |\n"
                            for n in range(1, count + 1))
            self.write(path, metadata(f"LH-FIX-REG-{i:02d}") + rows)

    def write(self, path, content):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

    def test_valid_baseline(self):
        self.assertEqual(dq.validate(self.root), [])

    def test_missing_frontmatter(self):
        self.write("docs/other.md", "# No metadata\n")
        self.assertTrue(any("frontmatter manquant" in e for e in dq.validate(self.root)))

    def test_readme_requires_frontmatter(self):
        self.write("docs/README.md", "# Missing\n")
        self.assertTrue(any("frontmatter manquant" in e for e in dq.validate(self.root)))

    def test_invalid_yaml(self):
        self.write("docs/example.md", "---\nid: [not closed\n---\n")
        self.assertTrue(any("frontmatter invalide" in e for e in dq.validate(self.root)))

    def test_duplicate_doc_id(self):
        self.write("docs/other.md", metadata("LH-FIX-001"))
        self.assertTrue(any("id duplique" in e for e in dq.validate(self.root)))

    def test_private_classification(self):
        self.write("docs/example.md", metadata("LH-FIX-001", classification="internal"))
        self.assertTrue(any("classification non publique" in e for e in dq.validate(self.root)))

    def test_invalid_document_status(self):
        self.write("docs/example.md", metadata("LH-FIX-001", status="ACCEPTED_BY_AI"))
        self.assertTrue(any("statut hors cycle" in e for e in dq.validate(self.root)))

    def test_invalid_date(self):
        self.write("docs/example.md", metadata("LH-FIX-001", updated_at="2026-99-99"))
        self.assertTrue(any("updated_at invalide" in e for e in dq.validate(self.root)))

    def test_canonical_gap(self):
        name, prefix, width, count = dq.REGISTRIES[0]
        file = self.root / name
        lines = file.read_text()
        lines = lines.replace(f"| `{prefix}-{2:0{width}d}` | Synthétique |\n", "")
        file.write_text(lines)
        self.assertTrue(any("manque=[2]" in e for e in dq.validate(self.root)))

    def test_canonical_duplicate(self):
        name, prefix, width, count = dq.REGISTRIES[1]
        file = self.root / name
        rows = file.read_text().replace(
            f"| `{prefix}-{2:0{width}d}` |",
            f"| `{prefix}-{1:0{width}d}` |", 1)
        file.write_text(rows)
        self.assertTrue(any("doublons=[1]" in e for e in dq.validate(self.root)))

    def test_prose_reference_not_canonical(self):
        with (self.root / dq.REGISTRIES[0][0]).open("a") as f:
            f.write("\nSource mention: LH-OPEN-001, BF-LH-001..004.\n")
        self.assertEqual(dq.validate(self.root), [])

    def test_broken_local_link(self):
        self.write("docs/example.md", metadata("LH-FIX-001") + "[Broken](absent.md)\n")
        self.assertTrue(any("cible absente" in e for e in dq.validate(self.root)))

    def test_broken_html_image(self):
        self.write("README.md", '<img src="docs/absent.png" alt="test">\n')
        self.assertTrue(any("cible absente" in e for e in dq.validate(self.root)))

    def test_unsafe_traversal(self):
        self.write("docs/example.md", metadata("LH-FIX-001") + "[Out](../../../../tmp/foo)\n")
        self.assertTrue(any("lien hors depot" in e for e in dq.validate(self.root)))

    def test_fenced_fake_link_ignored(self):
        self.write("docs/example.md", metadata("LH-FIX-001") + "```md\n[Fake](absent.md)\n```\n")
        self.assertEqual(dq.validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
