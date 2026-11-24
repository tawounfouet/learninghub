---
id: LH-DOM-UBI-001
title: "LearningHub - Langage ubiquitaire"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Langage ubiquitaire

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| Terme | Définition de travail |
|---|---|
| `Course` | Identité logique d'une formation |
| `CourseVersion` | Instantané de contenu et de politiques pédagogiques |
| `Enrollment` | Inscription d'un apprenant à une version ou un parcours |
| `AccessGrant` | Droit explicite de consulter ou participer |
| `AccessPolicy` | Règles d'évaluation de l'accès au moment de la demande |
| `Assessment` | Activité évaluable rattachée à une version |
| `Attempt` | Tentative individuelle, potentiellement soumise |
| `GradeDecision` | Résultat de notation historisé |
| `CompletionPolicy` | Critères de réussite ou d'achèvement versionnés |
| `CompletionRecord` | État calculé et justifié d'un parcours |
| `Credential` | Attestation ou justificatif issu d'un achèvement admissible |
| `EntitlementMirror` | Projection locale d'un droit émis par CommerceHub |
| `Cohort` | Groupe pédagogique ou temporel dont l'autorité reste à définir |
| `Outbox` | Événement fiable persisté avec la transaction source |
| `IdempotencyKey` | Identifiant de commande permettant de détecter les répétitions |
| `Tenant` | Frontière contractuelle d'isolation des données |

Une `Enrollment` n'est ni un achat ni une preuve automatique de réussite.
