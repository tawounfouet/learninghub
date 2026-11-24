---
id: LH-DOM-MOD-001
title: "LearningHub - Modèle de domaine candidat"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Modèle de domaine candidat

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Agrégats et relations structurantes

`Course -> CourseVersion -> Assessment -> Attempt -> GradeDecision`

En parallèle : `Learner -> Enrollment -> AccessGrant` et `Enrollment + GradeDecision + CompletionPolicy -> CompletionRecord -> Credential`.

| Ensemble | Autorité locale | Responsabilité |
|---|---|---|
| Catalog | LearningHub | Identité et publication des versions |
| Learning / Enrollment | LearningHub | Inscription et parcours |
| Access | LearningHub | Contrôle des droits pédagogiques |
| Assessment | LearningHub | Tentatives, notes et provenance |
| Completion | LearningHub | Décision de réussite |
| Credentials | LearningHub | Attestations et statut de validité |
| Commerce bridge | CommerceHub en source | Reprise contractuelle d'un droit externe |
| Project bridge | ProjectHub en source | Références à une cohorte ou un projet |

## Cycle cible

Le modèle privilégie des agrégats transactionnels compacts, des événements contractuels versionnés et la séparation entre écriture canonique et projection. Les frontières techniques exactes restent des sujets d'ADR, pas une obligation de microservices.
