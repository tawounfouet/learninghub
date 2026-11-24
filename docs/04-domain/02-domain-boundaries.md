---
id: LH-DOM-BOUND-001
title: "LearningHub - Frontières et intégrations"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Frontières et intégrations

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| Domaine | Fait dont il est propriétaire | Ce qu'il ne doit pas décider |
|---|---|---|
| LearningHub | Publication, inscription, note, réussite, credential pédagogique | Paiement, facture, remboursement |
| CommerceHub | Commande, paiement, droit commercial, révocation économique | Note, score, réussite |
| ProjectHub | Projet, échéance, coordination, cohorte si décidée | Résultat individuel d'un quiz |
| Identity provider | Authentification et identité externe | Inscription, achievement, autorisation métier complète |

## Règles de contrat

- Aucun couplage direct par lecture des tables d'un autre produit.
- Les ID externes sont typés par `source_system` et version de contrat.
- Un événement entrant est non autoritatif tant que son émetteur, sa signature, sa version et son mapping ne sont pas qualifiés.
- Les consommations doivent être idempotentes, observables et rejouables.
- Les modifications de droits doivent avoir une stratégie de fraîcheur et de réconciliation.

Les intégrations CommerceHub R2, ProjectHub R3 et standards R4 sont hors chemin critique du R1 gratuit.
