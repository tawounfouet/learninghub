---
id: LH-QA-DOC-001
title: "LearningHub - Checklist de qualité documentaire"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Checklist de qualité documentaire

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Contrôles techniques

- [ ] Les tests synthétiques `python -m unittest discover -s tests -p 'test_docs_quality.py' -v` réussissent.
- [ ] `python scripts/docs_quality.py --strict` renvoie zéro erreur.
- [ ] Les frontmatters sont publics, complets et cohérents.
- [ ] Les cinq registres canoniques conservent leurs identifiants stables.
- [ ] Tous les liens relatifs sont valides.
- [ ] Le workflow GitHub Actions de la PR apparaît en succès sur le **SHA courant**.

## Contrôles éditoriaux et métier humains

- [ ] Les noms de commande et événement sont alignés avec la source normative R0.
- [ ] Les URLs R1 utilisent le préfixe candidat et indiquent leur statut `PROPOSED`.
- [ ] Aucune information privée ou personnelle n'a été copiée depuis le corpus de travail.
- [ ] Les écarts `LH-REC-*` demeurent visibles et ne sont pas déclarés résolus sans décision.
- [ ] Les exemples ne sont pas présentés comme fonctionnalités ou tests applicatifs effectivement exécutés.
- [ ] Les exceptions, les droits de réutilisation et les approbations sont vérifiés explicitement.

Le workflow n'a pas de pouvoir d'approbation. Voir [politique de publication](../PUBLICATION-POLICY.md).
