---
id: LH-QA-DOC-001
title: "LearningHub - Checklist de qualité documentaire"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Checklist de qualité documentaire

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Contrôles à effectuer par PR

- [ ] Chaque fichier porte des métadonnées `id`, `title`, `version`, `status`, `classification`, `created_at`, `updated_at`.
- [ ] Tous les liens relatifs pointent vers un fichier présent.
- [ ] Aucune image privée ou ressource sous droit tiers n'est insérée sans autorisation.
- [ ] Aucune donnée personnelle d'apprenant, clé, token ou identifiant d'environnement réel n'apparaît.
- [ ] Les statuts de livraison, d'acceptation et de tests ne sont pas exagérés.
- [ ] Les IDs de besoins, décisions et événements ne sont pas silencieusement renumérotés.
- [ ] Les assertions qui portent sur des tests incluent des liens vers la preuve exécutée.
- [ ] Les contradictions entre R0 et R1 sont soit résolues par ADR, soit listées comme questions ouvertes.

## Automatisation envisagée

Linter Markdown, liens internes, validation YAML, recherche de secrets et contrôle des IDs. Ces protections ne sont pas activées par la seule présence du présent fichier.
