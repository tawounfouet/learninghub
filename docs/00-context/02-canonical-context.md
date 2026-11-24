---
id: LH-CTX-CAN-001
title: "LearningHub - Contexte canonique"
version: "0.1.0"
status: draft
classification: public
created_at: "2026-11-24"
updated_at: "2026-11-24"
---

# LearningHub - Contexte canonique

> **Baseline publique candidate.** Cette page est un document de cadrage. Elle ne prouve ni implémentation, ni validation métier, ni approbation de mise en production.

LearningHub a pour vocation de gérer la **vérité pédagogique** : contenu et version des cours, inscriptions, droits d'accès pédagogiques, évaluations, décisions de notes, réussite et justificatifs éventuels.

## Séparations fondamentales

| Concept | Responsabilité |
|---|---|
| `Course` | Identité durable d'un cours |
| `CourseVersion` | Contenu et règles figés à la publication |
| `Enrollment` | Relation d'inscription à une version |
| `AccessGrant` | Droit pédagogique contextualisé, non assimilé à un paiement |
| `Attempt` et `GradeDecision` | Travail soumis et décision de notation |
| `CompletionRecord` | Résultat de réussite selon une politique |
| `Credential` | Document émis à partir d'un résultat admissible |
| `EntitlementMirror` | Projection d'un droit commercial émis ailleurs |

CommerceHub reste autorité des opérations commerciales ; ProjectHub reste autorité du pilotage des initiatives et cohortes qu'il détient. Une intégration transmet un **fait** ou une **référence**, pas un transfert implicite d'autorité.

## Séquencement

- **R0** : domaine, transitions, invariants, politiques, contrats et ADR candidates.
- **R1** : cours Python publié, inscription gratuite, accès autorisé, quiz noté, réussite enregistrée, attestation simple optionnelle.
- **R2** : intégration des droits commerciaux avec CommerceHub.
- **R3** : intégration des projets/cohortes avec ProjectHub.
- **R4+** : standards LMS et fonctionnalités avancées en fonction des besoins validés.

Ces horizons restent à confirmer. Le jalon R1 n'est pas un programme d'implémentation déjà exécuté.
