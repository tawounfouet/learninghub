---
id: LH-ARCH-DATA-001
title: "LearningHub - Modèle relationnel R1 et migrations réconciliés"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Modèle relationnel R1 et migrations réconciliés

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Référence

Sources : `R1_LEARNINGHUB_ENTITY_RELATIONSHIP_DIAGRAM.md` et `R1_LEARNINGHUB_DATABASE_SCHEMA_AND_MIGRATIONS.md` (`PROPOSED`). Le dictionnaire physique R1 décrit **22 tables candidates** et pas seulement les dix entités simplifiées du premier index.

## Tables R1 recensées

| Zone | Tables candidates proposées |
|---|---|
| Identity & Tenancy | `lh_organization`, `lh_membership`, `lh_learner_profile` |
| Catalog & snapshots | `lh_course`, `lh_course_version`, `lh_module_snapshot`, `lh_lesson_snapshot`, `lh_assessment_version`, `lh_question_snapshot` |
| Enrollment & Access | `lh_enrollment`, `lh_access_grant`, `lh_lesson_progress` |
| Assessment & evidence | `lh_attempt`, `lh_submission`, `lh_grade_decision` |
| Completion & Credentials | `lh_completion_policy_snapshot`, `lh_completion_record`, `lh_credential` |
| Infrastructure & audit | `lh_idempotency_record`, `lh_outbox_event`, `lh_inbox_event`, `lh_audit_decision` |

## Points bloquants avant migrations

- FK tenant-scopées et accès inter-organisation interdits même par référence directe.
- Unicité d'un Enrollment ouvert, y compris le comportement SQL des valeurs `NULL` de cohorte.
- Immutabilité et réutilisation contrôlée des CourseVersion et AssessmentVersion.
- `GradeDecision` historisée, append-only selon modèle retenu.
- Révision optimiste et clés d'idempotence transactionnelles.
- Append outbox atomique, inbox et contrôle de réémission.
- Choix documenté entre filtres + FK, RLS PostgreSQL, ou défense combinée.

Le plan source propose un séquencement `expand -> backfill -> contract` et des tests avec PostgreSQL réel. **Aucune migration n'est déclarée exécutée ici.** Les DDL source restent à revoir avec les arbitrages R0.

Voir [réconciliation](07-r0-r1-source-reconciliation.md).
