---
id: LH-ARCH-INDEX
title: "LearningHub - Index architecture R0/R1"
version: "0.2.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Index architecture R0/R1

> **Synthèse publique R0/R1 - draft.** Les éléments tirés des spécifications de conception sont des contrats candidats, pas des interfaces livrées ni des décisions approuvées. Les originaux restent hors de ce dépôt public.

| Document | Sujet |
|---|---|
| [Architecture](00-architecture-baseline.md) | Cible Django/DRF, Next.js, PostgreSQL, outbox |
| [Machines d'état R0](01-state-machines-and-invariants.md) | Sept agrégats et états réconciliés |
| [Commandes et événements R0](02-commands-events-errors.md) | Types filaires R0 proposés |
| [Données R1](03-data-model-and-migrations.md) | Dictionnaire des 22 tables candidates |
| [API R1](04-api-and-event-contracts.md) | Préfixe proposé et 25 routes |
| [ADR](05-adr-register.md) | Registre public candidat, non encore réconcilié au registre source |
| [Vertical slice](06-vertical-slice-implementation-plan.md) | Programme de réalisation proposé |
| [Réconciliation](07-r0-r1-source-reconciliation.md) | 13 écarts identifiés et actions de clôture |

Les documents sources complets sont conservés séparément. Les synthèses corrigées ne sont pas une source normative approuvée tant que les décisions de mise en oeuvre ne sont pas prises.
