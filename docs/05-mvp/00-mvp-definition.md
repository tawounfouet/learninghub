---
id: LH-MVP-DEF-001
title: "LearningHub - Définition du MVP R1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Définition du MVP R1

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Scénario de référence

Un auteur publie un cours Python. Un apprenant s'y inscrit **gratuitement**, obtient un accès pédagogique vérifié, réalise un quiz, reçoit une décision de note et voit son achèvement calculé. Une attestation simple peut être produite si la policy et le périmètre le permettent.

## Critères de sortie

- Les transitions du parcours sont cohérentes, versionnées et transactionnelles.
- Les cas de refus existent et sont couverts par des tests négatifs.
- Les résultats d'évaluation peuvent être reconstruits et expliqués.
- Les opérations répétées ne produisent pas de doubles écritures non contrôlées.
- Les événements métier sont reliés à leur opération source.
- Les tests d'isolation des données et de droits sont exécutés et documentés.
- Les migrations, sauvegardes et procédures de restauration ont des preuves proportionnées à l'environnement.

L'exécution d'un test technique ne vaut pas approbation du produit ni autorisation de traiter des données réelles.
