---
id: LH-ARCH-R1-001
title: "LearningHub - Plan de réalisation vertical slice R1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Plan de réalisation vertical slice R1

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Objectif

Obtenir une preuve de bout en bout : cours Python publié, apprenant inscrit gratuitement, accès vérifié, quiz soumis et noté, réussite calculée, credential optionnel.

## Ordre proposé

| Séquence | Travail | Condition de sortie |
|---|---|---|
| S0 | Bootstrap, identité, conventions CI | Tests de base et refus inter-tenant définis |
| S1 | CourseVersion et publication | Invariant publication vérifié |
| S2 | Enrollment + AccessGrant | Contrôle d'accès et révocation vérifiés |
| S3 | Assessment + Attempt + GradeDecision | Note reproductible |
| S4 | CompletionRecord | Réussite expliquée et testable |
| S5 | Credential simple (optionnel) | Émission et vérification cohérentes |
| S6 | Outbox, audit et résilience | Scénarios répétition, concurrence et restauration |
| S7 | Revue d'acceptation | Preuves, réserves et GO/NO-GO documentés |

Le plan source `R1_LEARNINGHUB_VERTICAL_SLICE_IMPLEMENTATION_PLAN.md` contient un découpage plus fin. Cette page est l'index de pilotage public et n'annonce aucun ticket terminé.

## Points de contrôle

- R0 : stabiliser ownership, FSM, erreurs et noms d'événements.
- S0 : contrôler la reproductibilité de l'environnement de développement.
- S1-S4 : rattacher chaque PR à une exigence et à un test.
- S6 : démontrer les refus, retries, sécurité et audit.
- S7 : séparer verdict de prototype et autorisation de déployer.
