---
id: LH-GOV-COLLAB-001
title: "LearningHub - Collaboration GitHub et revues"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Collaboration GitHub et revues

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Circuit de contribution

Une modification structurante suit le chemin `Issue -> branche courte -> commit -> pull request -> revue -> CI -> merge`. Une demande d'ajout dans la documentation doit expliquer **le besoin, le périmètre, le niveau de preuve, les documents affectés et le critère d'acceptation**.

| Type | Exemple de branche | Sujet de revue |
|---|---|---|
| Documentation | `docs/learninghub-baseline` | Confidentialité, sources et liens |
| Conception | `design/enrollment-fsm` | Invariants, conflits et contrats |
| Fonctionnalité | `feat/course-publication` | Parcours, tests et migrations |
| Correction | `fix/access-guard` | Scénario reproduit, test de non-régression |

## Conventions

- Commit en impératif, par exemple `docs: specify enrollment boundaries`.
- Une PR contient objectif, changements, risques, scénarios testés, résultats et limites.
- Les décisions ADR ne sont pas acceptées par le seul fait de merger une PR.
- Une revue de code n'autorise pas à exposer des notes ou données d'apprenants.
- Si une action d'agent IA a aidé à préparer une proposition, le responsable humain en vérifie le résultat et les sources.

## Definition of Ready d'une PR R1

Exigence identifiée ; invariant et garde documentés ; contrat API ou événement versionné ; migration et rollback envisagés ; tests positifs, négatifs et de concurrence prévus ; critères de preuve explicités. Aucun résultat de CI ou d'intégration n'est présumé réussi sans lien vers l'exécution.
