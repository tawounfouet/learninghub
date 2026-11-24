---
id: LH-ARCH-API-001
title: "LearningHub - Contrats API R1 réconciliés"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Contrats API R1 réconciliés

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

## Source canonique candidate

`R1_LEARNINGHUB_API_AND_EVENT_CONTRACTS.md` propose le préfixe `/api/v1/learning/`. Les **25 routes du catalogue** sont proposées ; aucune n'est déclarée accessible sur un serveur.

Les exemples de première baseline comme `/api/v1/courses/`, `/api/v1/grade-decisions/` ou `/api/v1/access-grants/` ne sont **pas** les URLs approuvées. Une partie des opérations passe par des *commandes métier*, pas par un CRUD public sur chaque agrégat.

| ID source | Méthode | Chemin relatif au préfixe | État |
|---|---|---|---|
| API-001 | GET | `courses` | P0 |
| API-002 | GET | `courses/{course_id}` | P0 |
| API-003 | GET | `course-versions/{id}/syllabus` | P0 |
| API-004 | POST | `course-versions` | P0 |
| API-005 | POST | `course-versions/{id}/submit-review` | P0 |
| API-006 | POST | `course-versions/{id}/request-changes` | P0 |
| API-007 | POST | `course-versions/{id}/publish` | P0 |
| API-008 | POST | `course-versions/{id}/retire` | P1 |
| API-009 | POST | `enrollments` | P0 |
| API-010 | GET | `me/enrollments` | P0 |
| API-011 | GET | `enrollments/{id}` | P0 |
| API-012 | POST | `enrollments/{id}/activate` | P0 interne |
| API-013 | POST | `enrollments/{id}/suspend` | P1 |
| API-014 | POST | `enrollments/{id}/resume` | P1 |
| API-015 | POST | `enrollments/{id}/cancel` | P1 |
| API-016 | GET | `lessons/{id}/access` | P0 |
| API-017 | POST | `lessons/{id}/complete` | P0 |
| API-018 | GET | `enrollments/{id}/progress` | P0 |
| API-019 | POST | `assessments/{id}/attempts` | P0 |
| API-020 | POST | `attempts/{id}/start` | P0 |
| API-021 | POST | `attempts/{id}/submit` | P0 |
| API-022 | GET | `attempts/{id}` | P0 |
| API-023 | POST | `enrollments/{id}/evaluate-completion` | P0 interne |
| API-024 | GET | `enrollments/{id}/completion` | P0 |
| API-025 | GET | `credentials/{id}/verify` | P1 sous flag |

**API-012 et API-023 :** la source propose de privilégier une orchestration transactionnelle interne ou un namespace interne non exposé au navigateur.

## Règles transversales à stabiliser

- Les permissions par rôle et objet demeurent serveur et tenant-scopées.
- La commande de soumission doit être idempotente et respecter les dates limites.
- `If-Match` et `expected_revision` requièrent une convention unique.
- Les réponses d'échec sont des Problem Details RFC 9457.
- Le fragment OpenAPI de travail ne couvre **que quatre routes** : il ne prouve pas la conformité des 25 routes proposées.
- Les événements métiers sont des faits post-commit, soumis au registre R0 et à leurs JSON Schema.

## Arbitrages ouverts

Le registre des décisions source `API-R1-ADR-01..12` couvre notamment base path, idempotence, erreur de rejet de completion, compatibilité d'événements, révocation de ressources protégées et durée de conservation. Ces décisions restent ouvertes.

Voir [registre des écarts](07-r0-r1-source-reconciliation.md) et [tests R1](../06-validation/01-test-strategy-and-acceptance.md).
