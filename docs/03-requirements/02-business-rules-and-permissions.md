---
id: LH-REQ-RULE-001
title: "LearningHub - Règles métier et permissions"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Règles métier et permissions

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Invariants R1 candidats

1. Une `CourseVersion` publiée ne change pas silencieusement les règles et contenus utilisés pour noter.
2. Un `Enrollment` ne crée pas automatiquement un droit d'accès illimité.
3. L'accès n'est accordé que si un `AccessGrant` admissible existe et n'est pas révoqué ou expiré.
4. Une `Attempt` déjà soumise n'est pas modifiée comme si elle était encore en cours.
5. Chaque `GradeDecision` contient version, provenance et auteur/mécanisme.
6. Un `CompletionRecord` dépend d'une politique identifiable et de preuves d'évaluation admissibles.
7. Un `Credential` ne précède pas une réussite admissible.

## Matrice d'autorisations simplifiée

| Action | Auteur | Apprenant | Correcteur | Admin |
|---|---|---|---|---|
| Préparer un cours | Selon délégation | Non | Non | Selon périmètre |
| Publier une version | Selon délégation | Non | Non | Selon périmètre |
| S'inscrire | Non | Son propre compte | Non | Sur mandat explicite |
| Soumettre un quiz | Non | Inscription autorisée | Non | Non par défaut |
| Corriger | Non par défaut | Non | Selon affectation | Non par défaut |
| Lire une note individuelle | Cas autorisé | La sienne | Affectation limitée | Selon nécessité prouvée |

Ce tableau est **candidat** : aucune règle ne doit être traduite en permissions de production avant revue sécurité et tests de refus.
