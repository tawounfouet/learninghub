---
id: LH-REQ-NFR-001
title: "LearningHub - Exigences non fonctionnelles"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Exigences non fonctionnelles

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

| ID | Domaine | Critère candidat à formaliser |
|---|---|---|
| `LH-NFR-001` | Sécurité | Isolation entre organisations aux niveaux API, requêtes et exports |
| `LH-NFR-002` | Authentification | Session, identité et révocation robustes |
| `LH-NFR-003` | Intégrité | Atomicité des transitions critiques et constraints SQL |
| `LH-NFR-004` | Fiabilité | Idempotence des commandes et émission outbox |
| `LH-NFR-005` | Performance | Budgets latence/charge fixés après mesures R1 |
| `LH-NFR-006` | Observabilité | Traces de corrélation sans fuite de notes ou données sensibles |
| `LH-NFR-007` | Confidentialité | Minimisation des données, accès justifié, rétention documentée |
| `LH-NFR-008` | Accessibilité | Parcours clavier, lecteurs d'écran, erreurs compréhensibles |
| `LH-NFR-009` | Continuité | Sauvegarde, restauration et stratégie de migrations testées |
| `LH-NFR-010` | Portabilité | Export autorisé et structuré, avec références versionnées |

Les seuils chiffrés et la conformité ne sont pas déclarés atteints avant mesures et audits.
