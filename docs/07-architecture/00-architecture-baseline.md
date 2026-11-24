---
id: LH-ARCH-BASE-001
title: "LearningHub - Baseline architecture candidate"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Baseline architecture candidate

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Cible

- Backend : Python, Django et Django REST Framework.
- Frontend : Next.js et TypeScript.
- Persistance transactionnelle : PostgreSQL.
- Fiabilité asynchrone : outbox et worker de livraison.
- Architecture : monolithe modulaire et bounded contexts explicites, sans microservices imposés.

```text
[Client Web Next.js] -> [API Django / DRF] -> [Domaines LearningHub] -> [PostgreSQL]
                                            |
                                            +-> [Outbox] -> [Worker / Consumers]
```

## Règles de dépendance

1. Les agrégats ne dépendent pas des vues HTTP.
2. Les règles critiques sont exécutées côté serveur, en transaction si nécessaire.
3. Les adapters externes ne deviennent pas propriétaires des données pédagogiques.
4. Les lectures de droits doivent rester cohérentes avec la révocation et l'isolation des tenants.
5. Les événements sont versionnés et publiés après écriture transactionnelle.

Les versions précises des packages, l'hébergement et le fournisseur d'identité restent à décider via ADR.
