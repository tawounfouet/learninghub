---
id: LH-ARCH-FSM-001
title: "LearningHub - Machines à états et invariants R0"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Machines à états et invariants R0

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

Le travail R0 distingue plusieurs machines à états critiques ; les états exacts ci-dessous sont **illustratifs** tant que la spécification source n'est pas incorporée et signée.

| Agrégat | Transitions candidates | Garde cruciale |
|---|---|---|
| `CourseVersion` | `DRAFT -> PUBLISHED -> RETIRED` | Ne pas publier un cours incomplet |
| `Enrollment` | `ACTIVE -> COMPLETED / CANCELLED` | Une inscription cohérente par scope |
| `AccessGrant` | `ACTIVE -> EXPIRED / REVOKED` | Refuser l'accès après expiration |
| `Attempt` | `STARTED -> SUBMITTED -> GRADED` | Bloquer seconde soumission non idempotente |
| `CompletionRecord` | `PENDING -> ACHIEVED / NOT_ACHIEVED` | Appliquer policy versionnée |
| `Credential` | `ISSUED -> REVOKED` | Émission après réussite admissible |
| `EntitlementMirror` | État externe projeté, hors R1 | Ne pas confondre droit commercial et accès |

Pour chaque transition : command, acteur, précondition, transaction, événement, erreur, audit et test de refus. Les suppressions destructives doivent préserver les exigences d'audit et de conservation applicables.

**Attention :** la matrice R0 originale décrit une sémantique plus détaillée ; ne pas remplacer ses guards par cette table synthétique lors de l'implémentation.
