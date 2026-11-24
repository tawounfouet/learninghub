---
id: LH-DISC-FLOW-001
title: "LearningHub - Processus actuels et parcours cibles"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Processus actuels et parcours cibles

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Situation à investiguer

Dans plusieurs contextes, les cours, accès, questionnaires et relevés peuvent vivre dans des outils différents. Il faut **observer** les pratiques plutôt que déclarer que toutes les organisations rencontrent cette difficulté.

## Parcours cible R1

1. Un auteur prépare un cours Python en `DRAFT`.
2. Il publie une `CourseVersion` après vérification des règles requises.
3. Un apprenant autorisé crée son inscription à cette version.
4. Le système évalue un `AccessGrant` explicite avant toute consultation.
5. L'apprenant passe une tentative de quiz.
6. Une décision de note est consignée selon la version de règle applicable.
7. Une politique établit ou refuse l'achèvement.
8. Si le périmètre l'autorise, une attestation simple est émise.

Le parcours doit tester les refus : version retirée, accès expiré, inscription répétée, double soumission, absence de réussite et tentative inter-tenant.
