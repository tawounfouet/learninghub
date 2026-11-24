---
id: LH-DOC-INDEX
title: "LearningHub - Index de la documentation"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Index de la documentation

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

La documentation de LearningHub reprend les conventions de [ProjectHub](https://github.com/tawounfouet/projecthub/tree/main/docs) avec un contenu propre au LMS. Tous les livrables initiaux sont des **synthèses publiques candidate** de spécifications de travail antérieures. Les textes intégraux d'origine ne sont pas présumés importés ni approuvés.

## Navigation

| Dossier | Domaine | Entrée |
|---|---|---|
| `00-context/` | Historique, registre des sources, décisions, questions ouvertes | [Contexte canonique](00-context/02-canonical-context.md) |
| `01-product/` | Vision, stratégie et frontières du produit | [Vision](01-product/00-product-vision.md) |
| `02-discovery/` | Personas, besoins, workflows et recherche | [Discovery](02-discovery/README.md) |
| `03-requirements/` | Exigences, règles, accès et traçabilité | [Exigences](03-requirements/README.md) |
| `04-domain/` | Glossaire, agrégats, bounded contexts | [Domaine](04-domain/README.md) |
| `05-mvp/` | Définition R1, parcours, backlog | [MVP](05-mvp/README.md) |
| `06-validation/` | Scénarios, tests, preuves et critères GO/NO-GO | [Validation](06-validation/README.md) |
| `07-architecture/` | Architecture, états, contrats, modèle de données, ADR | [Architecture](07-architecture/README.md) |
| `quality/` | Qualité documentaire et contrôles | [Qualité](quality/README.md) |
| `reports/` | Comptes rendus d'exécution vérifiés | [Rapports](reports/README.md) |
| `assets/` | Illustrations et schémas publiables | [Assets](assets/README.md) |

Le répertoire `01-product/assets/` est également préparé pour les visuels propres au produit.

## Autorité des informations

1. **Source de travail** : artefacts originaux LearningHub, conservés séparément tant que leur publication intégrale n'est pas revue.
2. **Édition publique** : synthèse de conception dans ce dépôt, modifiable en pull request.
3. **ADR acceptée** : décision explicitement approuvée avec date et auteur habilité.
4. **Preuve d'exécution** : test, CI, migration ou pilote réellement exécuté et référencé.

Ne jamais confondre les niveaux 1 à 4. Les numéros de lots R0/R1 désignent des **horizons de conception** et non des releases déployées.

## Chaîne de traçabilité

`Expression du besoin -> Analyse -> Exigence -> Modèle -> Invariant -> Contrat -> Ticket -> Test -> Preuve -> Décision`

Les besoins `BF-LH-xxx`, tickets `LH-R1-xxx` et validations `VAL-LH-xx` cités constituent des identifiants de correspondance issus des travaux de conception. Leur présence ne signifie pas qu'une issue GitHub, un test ou une migration existe déjà.

## Règles de contribution

- Ajouter une provenance, une date et un statut à toute affirmation significative.
- Ne pas révéler d'informations personnelles d'étudiants, de clients ou d'organisations.
- Ne pas copier des sources privées, des fichiers tiers ou des clés dans un dépôt public.
- En cas de désaccord entre documents, ouvrir un arbitrage et ne pas réécrire l'historique.
- Suivre [la politique de publication](PUBLICATION-POLICY.md) et [le guide de collaboration](COLLABORATION-BEST-PRACTICES.md).
