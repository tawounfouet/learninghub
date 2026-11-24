---
id: LH-QA-INDEX
title: "LearningHub - Qualité documentaire automatisable"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Qualité documentaire automatisable

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Installation et exécution locale

```bash
python -m pip install -r docs/quality/requirements.txt
python -m unittest discover -s tests -p 'test_docs_quality.py' -v
python scripts/docs_quality.py --strict
```

Le validateur `scripts/docs_quality.py` ne contacte aucun service externe et ne modifie pas le dépôt. Le workflow `.github/workflows/docs-quality.yml` est **proposé dans une pull request**, et ne deviendra actif sur `main` qu'après fusion. Un succès GitGuardian ne remplace pas les contrôles du validateur.

## Contrôles implémentés dans la proposition

| Contrôle | Périmètre |
|---|---|
| Frontmatter YAML | Tous les `docs/**/*.md`, y compris `README.md` |
| Métadonnées | `id/title/version/status/classification/created_at/updated_at` |
| Identifiants | Unicité des IDs documentaires dans `docs/` |
| Registres | `LH-OPEN-001..012`, `LH-DEC-001..008`, `LH-ADR-001..010`, `LH-UJ-01..09`, `LH-FR-001..010` |
| Liens locaux | Chemins Markdown, images, HTML ; existence, casse, traversée interdite |
| Fixtures | Scénarios positifs et négatifs synthétiques via `unittest` |

Le validateur regarde les **lignes canoniques en première colonne**, pas les références répétées ou les plages du registre interne `BF-LH-xxx`.

## Portée limitée

- Il ne valide pas les ancres internes après `#`, ni les liens HTTP(S), ni les droits de publication, ni les schémas OpenAPI/JSON Schema.
- Il ne certifie pas l'exactitude des états R0 ou de l'API R1 : voir le [registre de réconciliation](../07-architecture/07-r0-r1-source-reconciliation.md).
- Les checklists humaines et l'autorité d'approbation demeurent nécessaires.

Pour une revue avant fusion, consulter les checks de la PR, puis effectuer une revue de confidentialité et de justesse du contenu.
