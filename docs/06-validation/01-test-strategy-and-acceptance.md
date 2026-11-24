---
id: LH-VAL-TEST-001
title: "LearningHub - Tests et critères d'acceptation R0/R1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Tests et critères d'acceptation R0/R1

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Familles de tests

| Niveau | Objectif | Exemples |
|---|---|---|
| Unitaires | Transition et garde métier | Version non publiée, accès expiré |
| Modèle / DB | Contrainte et atomicité | Unicité Enrollment, tentative concurrente |
| API | Permissions et erreurs versionnées | 401/403/404/409/422 selon contrat |
| Événements | Enveloppe et réémission | Outbox, ordre causal, idempotence |
| E2E | Parcours utilisateur entier | Course -> Enrollment -> Attempt -> Completion |
| Sécurité | Isolation et fuite de données | Cross-tenant, accès horizontal |
| Exploitation | Reprise et visibilité | Migrations, rollback, restauration |

## Politique pour chaque transition d'état

Créer un test positif, au moins un test par garde, un cas interdit, un test de concurrence lorsque partagé et un cas de compatibilité d'événement si publié. Les résultats des travaux source R0 sont des matrices **de conception**, pas des campagnes de tests CI vérifiées dans ce nouveau dépôt.

## Conditions GO / NO-GO

- **GO conception :** arbitrages bloquants enregistrés et contrats cohérents.
- **GO implémentation R1 :** tickets, migrations, scénarios et permissions prêts pour revue.
- **GO production :** tests réellement exécutés, sécurité, restauration, observabilité et validation humaine documentées.

Aucun de ces GO n'est déclaré acquis dans cette baseline initiale.
