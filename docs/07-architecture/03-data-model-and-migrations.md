---
id: LH-ARCH-DATA-001
title: "LearningHub - Modèle relationnel et stratégie de migrations"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Modèle relationnel et stratégie de migrations

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Entités candidates R1

| Table conceptuelle | Liens majeurs | Contrainte à détailler |
|---|---|---|
| `course` | owner/tenant | Identifiant stable |
| `course_version` | course | Version unique ; contenu publié protégé |
| `assessment` | course_version | Policy et version cohérentes |
| `enrollment` | learner, course_version | Unicité selon scope et cohorte |
| `access_grant` | enrollment, source | Fenêtre temporelle et révocation |
| `attempt` | enrollment, assessment | Tentatives et deadlines |
| `grade_decision` | attempt | Historisation, version et auteur |
| `completion_record` | enrollment, policy | Provenance de la réussite |
| `credential` | completion_record | Émission contrôlée |
| `outbox_event` | agrégat, version | Livraison fiable |

## Stratégie de migration

1. Créer des schémas compatibles, constraints et index adaptés aux requêtes de sécurité.
2. Migrer données et code en étapes sûres, avec prétests des cas limites.
3. Vérifier les transitions, les références et les doublons en concurrence.
4. Prévoir sauvegarde et procédure de retour arrière ; les changements irréversibles nécessitent un plan de correction.
5. Tester sur données synthétiques multi-tenants.

L'ERD précis, les noms SQL, index et migrations versionnées de la spécification R1 restent à valider avant que cette synthèse serve de code source.
