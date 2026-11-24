---
id: LH-ARCH-API-001
title: "LearningHub - Contrats API et événements R1"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Contrats API et événements R1

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Ressources de l'API cible

| Domaine | Exemple de surface | Garde |
|---|---|---|
| Catalogue | `/api/v1/courses/` | Publication limitée aux auteurs autorisés |
| Versions | `/api/v1/course-versions/` | Version et cohérence |
| Inscriptions | `/api/v1/enrollments/` | Learner/scope |
| Accès | `/api/v1/access-grants/` | Contrôle de droit à chaque lecture |
| Quiz | `/api/v1/attempts/` | Deadline, ownership et idempotence |
| Notes | `/api/v1/grade-decisions/` | Permissions correcteur |
| Réussite | `/api/v1/completions/` | Provenance et policy |
| Justificatifs | `/api/v1/credentials/` | Éligibilité et validité |

**Chemins volontairement illustratifs** : ni routes implémentées ni contrat OpenAPI approuvé. Aucun endpoint de prod n'est prétendu disponible.

## Exigences de contrat

- Versionnement explicite des schémas et refus d'arguments inconnus critiques.
- Statuts HTTP et structures d'erreur harmonisés avec les contrats R0.
- Idempotency-Key sur commandes sensibles et preconditions concurrentes.
- Contrôle d'accès en profondeur, filtrage inter-tenant et absence de fuite par erreur de ressource.
- Événements avec event_id, type, version, occured_at, correlation_id, aggregate et contexte autorisé.

La publication des schémas OpenAPI/JSON Schema doit découler d'une autorité de contrat choisie et de tests de compatibilité.
