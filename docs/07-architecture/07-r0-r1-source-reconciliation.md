---
id: LH-ARCH-RECON-001
title: "LearningHub - Réconciliation des sources R0/R1 et plan d'arbitrage"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Réconciliation des sources R0/R1 et plan d'arbitrage

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Objet et méthode

Ce document rapproche les synthèses publiques fusionnées via la PR #1 des spécifications de conception R0/R1 datées du 24 novembre 2026. Les originaux (fichiers Markdown de travail) ont été lus pour cette revue, mais **ils ne sont pas importés intégralement dans le dépôt public**. La correspondance ci-dessous est donc une **réconciliation documentaire** et non une revue juridique ou une acceptation de contrats.

| ID d'écart | Constat entre baseline publique et source R0/R1 | Action documentée | Statut |
|---|---|---|---|
| `LH-REC-001` | La synthèse CourseVersion omettait `IN_REVIEW` | États et transitions R0 rétablis dans la [page FSM](01-state-machines-and-invariants.md) | Corrigé en documentation |
| `LH-REC-002` | Attempt omettait `CREATED`, `GRADING` et `INVALIDATED` | Liste exacte des états R0 publiée | Corrigé en documentation |
| `LH-REC-003` | CompletionRecord était résumé en `ACHIEVED/NOT_ACHIEVED` au lieu du modèle de revue | Liste `PENDING/ACHIEVED/REJECTED/UNDER_REVIEW/INVALIDATED` publiée | Corrigé en documentation |
| `LH-REC-004` | Credential et Enrollment étaient simplifiés | États source détaillés | Corrigé en documentation |
| `LH-REC-005` | EntitlementMirror était ramené à un statut unique | Deux axes `source_status` et `sync_status` explicités | Corrigé en documentation |
| `LH-REC-006` | Les événements du tableau R0 utilisaient des noms CamelCase illustratifs | Noms filaires `learning.*.v1` proposés rétablis | Corrigé en documentation |
| `LH-REC-007` | Les endpoints publics étaient des ressources CRUD illustratives avec mauvais préfixe | Préfixe `/api/v1/learning/` et catalogue des 25 routes source reproduits | Corrigé en documentation |
| `LH-REC-008` | Le modèle de persistance listait une dizaine d'entités conceptuelles | 22 tables R1 de la spécification de migration recensées | Corrigé en documentation |
| `LH-REC-009` | La nomenclature de rejet de CompletionRecord diverge entre les sources | ADR unique et migration des producteurs, tests et schémas nécessaires | **Ouvert, bloquant contrat** |
| `LH-REC-010` | `Idempotency-Key`, réponse replay, `If-Match` et versionnement sont encore discutés | Choisir les conventions et produire contrat approuvé + tests | **Ouvert, bloquant implémentation** |
| `LH-REC-011` | IDs `LH-ADR-* / LH-FR-*` publics créés pour synthèses, distincts de la nomenclature R0/R1 source | Établir mapping validé, ne pas fusionner les espaces sans décision | **Ouvert** |
| `LH-REC-012` | `R0_LEARNINGHUB_ADR_REGISTER.md` est cité dans l'index historique mais sa version intégrale n'a pas été récupérée lors de cette revue | Obtenir la source canonique avant d'annoncer les ADR correspondantes comme réconciliées | **Source à confirmer** |
| `LH-REC-013` | Le pack externe de 99 JSON Schema R0 n'est pas publié ni vérifié ici | Établir registre, droits, versions et tests de compatibilité | **Hors périmètre de cette PR** |

## Tables d'autorité

| Sujet | Document de conception faisant référence | État |
|---|---|---|
| Expression et problèmes | `00_LEARNINGHUB_EXPRESSION_DU_BESOIN.md`, `00A_LEARNINGHUB_ANALYSE_DU_BESOIN.md` | Proposition |
| Domaines et frontières | `LEARNINGHUB_DOMAIN_MODEL_AND_ARCHITECTURE.md`, `R0_LEARNINGHUB_DOMAIN_BOUNDARIES_AND_FIT_AUDIT.md` | Proposition |
| Machines et invariants | `R0_LEARNINGHUB_STATE_MACHINES_AND_INVARIANTS.md` | Proposition normative R0 |
| Noms filaires, enveloppes, erreurs | `R0_LEARNINGHUB_COMMANDS_EVENTS_AND_ERROR_CONTRACTS.md` | Proposition normative R0 |
| Tests de FSM | `R0_LEARNINGHUB_STATE_MACHINE_TEST_MATRIX.md` | Tests planifiés, non exécutés |
| Schéma / ERD / migration | `R1_LEARNINGHUB_ENTITY_RELATIONSHIP_DIAGRAM.md`, `R1_LEARNINGHUB_DATABASE_SCHEMA_AND_MIGRATIONS.md` | Proposition R1 |
| Contrats REST et événements | `R1_LEARNINGHUB_API_AND_EVENT_CONTRACTS.md` | Proposition R1 |
| Preuve QA et sortie | `R1_LEARNINGHUB_TEST_STRATEGY_AND_ACCEPTANCE.md` | Tests planifiés, non exécutés |
| Tranche fonctionnelle | `R1_LEARNINGHUB_VERTICAL_SLICE_IMPLEMENTATION_PLAN.md` | Plan, aucune fonctionnalité livrée |

## Gate de réconciliation avant réalisation

1. Valider l'index des sources, y compris le registre ADR manquant.
2. Figer les états/guards exacts et leurs contrats de persistance.
3. Trancher les noms d'événements divergents, la concurrence et le protocole de replay.
4. Vérifier que les 25 routes ont des spécifications et tests de contrat complets.
5. Ajouter des fixtures JSON Schema publiques autorisées et des tests par contrat.
6. Conserver une traçabilité `BF-LH -> R0 -> ticket LH-R1 -> test -> preuve -> décision`.

**Verdict :** documentation synthétique corrigée pour les écarts `001..008` ; ne pas déclarer de GO implémentation/production en l'absence des décisions `009..013` et des preuves associées.
