---
id: LH-REQ-FR-001
title: "LearningHub - Exigences fonctionnelles candidates"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Exigences fonctionnelles candidates

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| ID de synthèse | Exigence candidate R1 | Vérification envisagée |
|---|---|---|
| `LH-FR-001` | Créer un cours identifié indépendamment de ses versions | Identité stable du cours |
| `LH-FR-002` | Publier une version cohérente et verrouiller les champs pédagogiques | Mutation interdite après publication |
| `LH-FR-003` | Inscrire un apprenant à une version autorisée | Unicité et rattachement démontrés |
| `LH-FR-004` | Attribuer ou refuser un accès justifié | Refus sans `AccessGrant` admissible |
| `LH-FR-005` | Créer et soumettre une tentative de quiz | Idempotence et deadline contrôlées |
| `LH-FR-006` | Produire une décision de note historisée | Résultat attribué à la bonne tentative |
| `LH-FR-007` | Calculer un achèvement selon une règle versionnée | Résultat déterministe et retraçable |
| `LH-FR-008` | Émettre une attestation si les conditions sont remplies | Non-émission si conditions absentes |
| `LH-FR-009` | Journaliser les décisions importantes | Actor, contexte et horodatage |
| `LH-FR-010` | Exposer des interfaces accessibles via API et UI | Parcours auteur et apprenant démontrés |

Ces IDs `LH-FR` sont des **identifiants de synthèse publique nouveaux** et ne remplacent pas le registre source `BF-LH`. Les scénarios tests doivent rattacher chaque exigence aux cas de la [matrice](03-requirements-traceability.md).
