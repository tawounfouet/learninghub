---
id: LH-ARCH-CEE-001
title: "LearningHub - Commandes, événements et erreurs R0 réconciliés"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Commandes, événements et erreurs R0 réconciliés

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Autorité de conception

Référence : `R0_LEARNINGHUB_COMMANDS_EVENTS_AND_ERROR_CONTRACTS.md` (`PROPOSED`). Les noms ci-dessous reproduisent les types filaires proposés. Les alias CamelCase de la première baseline étaient **illustratifs** et ne constituent pas des événements canoniques.

| Commande métier | Type de commande proposé | Type d'événement versionné R0 |
|---|---|---|
| `SubmitForReview` | `learning.course_version.submit_for_review` | `learning.course_version.review_requested.v1` |
| `PublishCourseVersion` | `learning.course_version.publish` | `learning.course_version.published.v1` |
| `RetireCourseVersion` | `learning.course_version.retire` | `learning.course_version.retired.v1` |
| `RequestEnrollment` | `learning.enrollment.request` | `learning.enrollment.requested.v1` |
| `ActivateEnrollment` | `learning.enrollment.activate` | `learning.enrollment.activated.v1` |
| `SuspendEnrollment` | `learning.enrollment.suspend` | `learning.enrollment.suspended.v1` |
| `ResumeEnrollment` | `learning.enrollment.resume` | `learning.enrollment.resumed.v1` |
| `RecordCompletion` | `learning.enrollment.record_completion` | `learning.enrollment.completed.v1` |
| `CancelEnrollment` | `learning.enrollment.cancel` | `learning.enrollment.cancelled.v1` |
| `RevokeGrant` | `learning.access_grant.revoke` | `learning.access.grant.revoked.v1` |

**Attention au nommage :** les événements AccessGrant proposés utilisent `learning.access.grant.*.v1` alors que leurs commandes utilisent `learning.access_grant.*`. Ne pas normaliser arbitrairement les séparateurs sans ADR et migration de schémas.

## Enveloppe et fiabilité

Une commande indique l'acteur, le contexte tenant, le scope, la corrélation, une révision attendue si applicable et une clé d'idempotence. Un événement post-commit inclut un identifiant, une version de schéma, l'agrégat, sa révision, la provenance et l'heure de l'événement. Les événements sont persistés en outbox dans la même transaction et consommés de manière idempotente.

Le registre source documente un pack externe de **99 JSON Schema**, dont le contenu complet n'a pas été importé dans ce dépôt. La présence de cette synthèse n'atteste donc pas de la validation du pack ni de la compatibilité des producteurs.

## Contrats de refus et erreurs

Utiliser le format `application/problem+json` issu de RFC 9457, avec `error_code`, `correlation_id` et une `instance` sans données sensibles. Les erreurs proposées incluent `DUPLICATE_ENROLLMENT`, `COURSE_VERSION_IMMUTABLE`, `ATTEMPT_LIMIT_REACHED`, `COMPLETION_EVIDENCE_INSUFFICIENT`, `REVISION_CONFLICT` et `TENANT_SCOPE_MISMATCH`.

Ne pas réutiliser les codes illustratifs de la première baseline (`ENROLLMENT_CONFLICT`, `GRADE_POLICY_MISMATCH`, etc.) comme références contractuelles sans validation contre le registre complet.

## Divergence à fermer

Le registre R0 propose `learning.completion.rejected_after_review.v1` pour `RejectCandidate`. Le plan R1 et la stratégie QA demandent de résoudre sa coexistence éventuelle avec `completion.rejected.v1` avant publication. **Aucun alias de compatibilité n'est autorisé par cette page.**

Voir [réconciliation](07-r0-r1-source-reconciliation.md) et [contrats API R1](04-api-and-event-contracts.md).
