---
id: LH-GOV-PUB-001
title: "LearningHub - Politique de publication documentaire"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Politique de publication documentaire

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

## Public et privé

Le dépôt GitHub est public. Les documents originaux issus des phases de réflexion, les notes d'entretien, les jeux de données d'apprenants et les décisions internes restent hors de ce dépôt tant qu'une revue explicite n'a pas établi leur publication possible.

| Niveau | Destination | Exemple |
|---|---|---|
| `public` | GitHub après relecture | Vision, glossaire, contrats génériques |
| `internal` | Espace de travail privé | Roadmap non validée, arbitrages sensibles |
| `confidential` | Espace privé à accès restreint | Étudiants, notes, copies, données clients |
| `restricted` | Gestionnaire de secrets | Tokens, clés, credentials, détails exploitables de vulnérabilités |

## Prépublication obligatoire

1. Identifier l'auteur, la source et les droits de publication du texte et des images.
2. Retirer ou remplacer données personnelles, verbatims privés et captures réelles.
3. Vérifier que les décisions sont marquées `PROPOSED`, `ACCEPTED` ou `SUPERSEDED` selon leur état effectif.
4. Vérifier liens, identifiants, dates, termes et tableaux de traçabilité.
5. Soumettre une pull request pour relecture humaine avant fusion.

Publier un fichier ne signifie pas que les exigences, les ADR, les résultats des tests ou le MVP sont approuvés. Les modifications de données éducatives requièrent une étude propre aux traitements RGPD et à la politique de conservation.

## Source canonique et duplication

Le corpus d'analyse initial (`00`, `00A`, modèles R0 et plans R1) a fait l'objet de travaux séparés. Ce dépôt n'en contient pour l'instant que des **résumés publiables**. Les originaux ne doivent pas être importés en bloc pour obtenir artificiellement une parité documentaire.

## Gestion des versions

Tout Markdown de cadrage comporte `id`, `version`, `status`, `classification` et dates. Le statut documentaire suit `draft -> in-review -> approved -> superseded` ; les décisions métier ont leur propre cycle. Une nouvelle version doit préserver les liens avec les anciens identifiants.
