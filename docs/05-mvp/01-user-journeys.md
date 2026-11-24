---
id: LH-MVP-UJ-001
title: "LearningHub - Parcours utilisateurs candidats"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Parcours utilisateurs candidats

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| ID | Acteur | Parcours | Test de refus essentiel |
|---|---|---|---|
| `LH-UJ-01` | Auteur | Créer et publier CourseVersion | Publication sans contenu requis |
| `LH-UJ-02` | Apprenant | S'inscrire à un cours publié | Doublon et version non admissible |
| `LH-UJ-03` | Apprenant | Accéder au contenu | Droit absent, expiré, révoqué |
| `LH-UJ-04` | Apprenant | Démarrer et soumettre un quiz | Soumission après deadline |
| `LH-UJ-05` | Correcteur / système | Noter selon policy | Duplicata et mauvaise version |
| `LH-UJ-06` | Apprenant | Consulter la réussite expliquée | Résultat sans preuves nécessaires |
| `LH-UJ-07` | Système | Émettre une attestation optionnelle | Émission sans réussite admissible |
| `LH-UJ-08` | Administrateur | Révoquer un accès et auditer | Opération hors périmètre |
| `LH-UJ-09` | Exploitant | Rejouer une commande / un événement | Effet secondaire en double |

Chaque scénario devra recevoir des données de test fictives, un résultat attendu et un lien de preuve avant le GO.
