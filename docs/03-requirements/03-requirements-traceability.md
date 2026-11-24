---
id: LH-REQ-TRACE-001
title: "LearningHub - Matrice de traçabilité R0/R1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Matrice de traçabilité R0/R1

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| Besoin source | Conception associée | Tickets de référence | Preuve attendue |
|---|---|---|---|
| `BF-LH-007..012` | CourseVersion FSM | `LH-R1-010..014` | Tests version/publication |
| `BF-LH-015..020` | Enrollment, AccessGrant, AccessPolicy | `LH-R1-020..025` | Tests d'accès/refus |
| `BF-LH-025..029` | Attempt et GradeDecision | `LH-R1-030..034` | Tests notation |
| `BF-LH-030..031` | CompletionRecord | `LH-R1-040..044` | Validation réussite |
| `BF-LH-035` | Credential optionnel | `LH-R1-060..062` | Tests émission/validité |
| `BF-LH-001..004` | Tenant/identity | `LH-R1-003`, `006`, `073` | Tests cross-tenant |
| `BF-LH-050..052` | Audit, outbox et contrats | `LH-R1-070..072`, `075` | Tests événements |

Les IDs de tickets proviennent de la conception source R1. **Ne pas les confondre avec des issues GitHub créées ou des tests exécutés.** Ajouter les liens de PR, tests et captures de CI seulement après vérification.
