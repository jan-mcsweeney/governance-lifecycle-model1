**In brief.** The architecture's statement of intent, in French. It sets out why > the architecture exists — to connect governance domains operationally rather > than to replace any of them — whom it serves, five design principles beginning > with *audience precedes artefact*, and the four layers of which the > thirteen-stage lifecycle is the third. The lifecycle itself is documented in > English in [`lifecycle.md`](lifecycle.md).

**Architecture — « Cadre de cadres » — Cycle de vie de la gouvernance — août 2026**
**Model1, v0.1.0**


**Intention architecturale**

Les organisations opèrent de plus en plus à l’intersection de domaines de gouvernance qui se chevauchent : intelligence artificielle, protection de la vie privée, cybersécurité, gouvernance de l’information et conformité réglementaire. Des cadres matures existent dans chacun de ces domaines. Ce qui fait défaut, dans la plupart des organisations, c’est la connexion entre eux.

Une obligation naît dans un domaine et trouve son exécution dans une mesure de contrôle relevant d’un autre. Les éléments de preuve produits aux fins d’un audit dans un cadre constituent ceux dont une activité d’assurance a besoin dans un second. Une décision qui doit être prise avant qu’une action puisse être engagée repose sur l’évaluation des risques, sur l’avis juridique et sur les connaissances dont dispose déjà l’organisation — et elle est consignée, lorsqu’elle l’est, dans un système qui ne relève d’aucun de ces cadres.

Il revient ainsi aux praticiens d’intégrer, sur le plan opérationnel, ce que les cadres décrivent séparément.

Cette architecture de référence propose un modèle de gouvernance connecté : un cycle de vie unique auquel peuvent être rattachés les obligations, les contrôles, les éléments de preuve et l’assurance, afin que les relations entre eux soient visibles plutôt que présumées. Elle ne se substitue ni aux normes ISO ou NIST, ni au règlement européen sur l’IA, ni à la législation relative à la protection de la vie privée. Sa finalité est de les relier.

**À qui s’adresse-t-elle ?**

L’architecture est conçue pour la personne qui doit prendre une décision et être en mesure de la justifier.

Il peut s’agir du responsable de la gouvernance auquel il est demandé si un système peut être mis en œuvre, du spécialiste de l’assurance chargé de déterminer si un contrôle a effectivement fonctionné, du responsable de la protection de la vie privée qui doit établir ce qu’une obligation exige dans une situation donnée, ou encore de l’auditeur qui doit déterminer ce que révèle la trace documentaire. Chacun a besoin d’informations différentes ; tous doivent pouvoir les rattacher à une source identifiable.

Le public précède l’artefact. Tel est le premier principe de conception, dont découle tout le reste. Avant de concevoir un cadre, un registre, un tableau de bord ou un document, une question prévaut : de quelles informations ce public a-t-il besoin pour prendre, avec confiance, une décision solide et fondée sur des éléments probants ?

Il ne s’agit pas d’un principe rédactionnel. Il détermine le contenu même de l’architecture. Le filtre d’admissibilité existe parce qu’une personne doit pouvoir décider sur la base d’informations suffisantes. La preuve constitue une étape, plutôt qu’un sous-produit, parce que l’assurance a besoin d’un objet à examiner. Le caractère actionnable est évalué indépendamment de la preuve, car une constatation sur laquelle personne ne peut agir ne sert aucune décision. 


**Principes**

Le public précède l’artefact. Les informations nécessaires à une décision déterminent ce qui doit être construit.

La gouvernance permet la décision. Un cadre de gouvernance qui ne débouche pas sur une décision à un point défini demeure descriptif ; il ne constitue pas une gouvernance.

La preuve fonde la confiance. Les traces existent parce que les contrôles ont fonctionné. Elles constituent un produit de l’architecture, et non une documentation élaborée parallèlement à celle-ci.

L’assurance valide la gouvernance. La confirmation indépendante est ce qui distingue un système dont le fonctionnement est établi d’un système dont le fonctionnement est simplement affirmé.

L’amélioration continue pérennise la capacité. Ce que révèle le cycle revient au cadre qui l’a autorisé. Un cycle de vie qui ne se referme pas est un pipeline. 


**Les quatre couches**

Couche 1 — Finalité. Pourquoi l’architecture existe : relier opérationnellement les domaines de gouvernance plutôt que se substituer à l’un quelconque d’entre eux.

Couche 2 — Principes. Les cinq principes énoncés ci-dessus. Ils sont pérennes et indépendants de tout domaine ou de toute juridiction.

Couche 3 — Architecture opérationnelle. Le cycle de vie en treize étapes, le filtre d’admissibilité, le moteur de cotation des enjeux et le registre des obligations. Il s’agit d’une composante de l’architecture, et non de l’architecture dans son ensemble.

Couche 4 — Évolution. L’architecture est conçue pour intégrer des domaines qui ne sont pas encore traités — les marchés publics, la gouvernance des données et ceux qui viendront ensuite. La couche 3 évolue ; les couches 1 et 2 deme.
