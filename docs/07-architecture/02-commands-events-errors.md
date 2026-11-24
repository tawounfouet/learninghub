---
id: LH-ARCH-CEE-001
title: "LearningHub - Commandes, événements et erreurs R0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Commandes, événements et erreurs R0

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Contrats de référence

Une commande doit inclure l'acteur, le tenant, le scope, l'identifiant de corrélation, la version attendue si nécessaire et une clé d'idempotence pour les effets répétables.

| Commande candidate | Événement candidat | Erreur à modéliser |
|---|---|---|
| `PublishCourseVersion` | `CourseVersionPublished` | `COURSE_VERSION_NOT_READY` |
| `EnrollLearner` | `LearnerEnrolled` | `ENROLLMENT_CONFLICT` |
| `GrantLearningAccess` | `LearningAccessGranted` | `GRANT_NOT_AUTHORIZED` |
| `SubmitAttempt` | `AttemptSubmitted` | `ATTEMPT_ALREADY_SUBMITTED` |
| `RecordGradeDecision` | `GradeDecisionRecorded` | `GRADE_POLICY_MISMATCH` |
| `EvaluateCompletion` | `CompletionEvaluated` | `COMPLETION_EVIDENCE_MISSING` |
| `IssueCredential` | `CredentialIssued` | `CREDENTIAL_NOT_ELIGIBLE` |

**Noms et codes ci-dessus : candidats de synthèse, non contrats canoniques figés.** Reprendre les identifiants du document R0 source validé avant d'implémenter ou de publier un SDK.

## Garanties attendues

- Refus autorisés/denied en cohérence avec les scopes.
- Contrôle des doublons et des commandes concurrentes.
- Outbox atomique, idempotence des consommateurs et gestion des erreurs.
- Problèmes API structurés avec codes stables, sans divulguer de donnée sensible.
- Compatibilité explicite lors d'une modification de schéma d'événement.
