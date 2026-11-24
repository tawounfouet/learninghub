# LearningHub

**LearningHub** est un projet de plateforme d'apprentissage et de gestion de formations (LMS), conçu autour du parcours pédagogique, de l'inscription, du contrôle d'accès, de l'évaluation et de la réussite.

> **Statut : conception R0 / préparation d'un vertical slice R1.** Ce dépôt public contient une première baseline documentaire, pas une application livrée ni une validation de mise en production.

## Documentation

La documentation est organisée selon la convention établie pour [ProjectHub](https://github.com/tawounfouet/projecthub/tree/main/docs), adaptée au domaine pédagogique.

- [Entrer dans la documentation](docs/README.md)
- [Vision et stratégie produit](docs/01-product/00-product-vision.md)
- [Exigences et permissions](docs/03-requirements/README.md)
- [Domaine et intégrations](docs/04-domain/README.md)
- [MVP R1](docs/05-mvp/README.md)
- [Validation](docs/06-validation/README.md)
- [Architecture et décisions](docs/07-architecture/README.md)
- [Politique de publication](docs/PUBLICATION-POLICY.md)

## Parcours R1 envisagé

```text
Auteur -> Cours -> Version publiée
                    |
Apprenant -> Inscription -> Droit d'accès -> Quiz -> Notation
                                                |
                                      Réussite vérifiable
                                                |
                                      Attestation (option)
```

Les intégrations avec CommerceHub (droits commerciaux), ProjectHub (pilotage et cohortes) et les standards LMS restent des étapes ultérieures sous contrat explicite. Une identité partagée ne signifie pas un partage automatique des données ou des autorisations.

## Principes

1. Séparer les faits, propositions, validations et preuves exécutées.
2. Distinguer les domaines LearningHub, CommerceHub et ProjectHub.
3. Ne jamais déduire un accès pédagogique d'un paiement sans vérifier le droit associé.
4. Traiter le modèle métier, les permissions et les tests comme des fondations de l'application.
5. Ne pas publier automatiquement de sources privées ni d'informations sur des apprenants réels.

## Contribution et licence

Les règles de contribution et de publication figurent dans `docs/`. La licence du logiciel reste à décider. Aucune permission de réutilisation du code n'est implicite en l'absence d'une licence explicite.
