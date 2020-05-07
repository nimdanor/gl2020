
Aujourd'hui

15" Gestion sociale.

15" de retour sur vos interviews.

75" d'interview -> les même binomes mais l'autre "client"

30" retour plus préci sur les rendu de la semaine. 

Reste du temps on vous aide a faire le travail de la semaine prochaine. 




 Globalement dans les clous pour une première fois.


Petits problèmes de validation des formats de fichier, (bool): True, usecaseI.md, problème de case (mod != MOD), mon script peut mieux faire.

 
Merci a celui qui a proposé un pull request sur le TODO.  Je vais en ajouter. ;)

------

Erreur principales:
1° confondre personne/role/acteurs/partie prenantes.
2° Pas de cohérence entre les documents, les mots utilisés dans les résumés et les objectifs sont pas dans le glossaire.
 C'est quoi un plat, une entrée, une pizza, un voeux.
 -> assurer vous que les groupes nominaux que vous utilisez dans les resumés, les objectifs, les rôles, le scénario nominal. 

3° Les cas d'utilisation partiels. Pas de cas d'utilisation pour les sénarios alernatifs.
    Les uses/extends.  
4° l'abscence d'héritage dans la définition des acteurs.  Login !!
Cela vous fera gagner du temps car vous ecrirer qu'une seule fois les choses.

5° Vous n'avez pas vérifié pour différents ensembles de données nécessaires au fonctionnement de vos applications.
    l'existance d'un couple acteur/use case permettant le chargement/edition/import/etc de ces données.
     **Elles arrivent pas magie dans le logiciel!**

6° Des glossaires faibles -> anti-trumpisme : la vérité mais sans intéret.

7° les MOD ! 
PAS D'acteurs dans le MOD SVP !!!!!!!!!!!!!!!!!!!!!!

@startuml

actor X
actor y

x --|> y 
@enduml

















C'est quoi un mash up ?



Elements du glossaire:
plat
boisson
pizza = un ensemble d'ingrédients
note = 
entrée
ingrédient
commande
acteurX= lien vers le fichier acteurX.md qui contient la description de l'acteur.










# Plusieurs fois le même rôle
nom:principal:humain:formation:role
Commerciaux:true:true:true:Consulter le plan de charges. Il peut egalement pre reserver tel intervenant pour un projet.
Intervenants:true:true:true:Consulter le plan de charges.
Chef de projet:true:true:true:Peut consulter et/ou modifier la repartition des intervenants sur les projets et dans le temps.
CEO:true:true:true:Consulter et/ou modifier toutes les donnees (plan de charge, budget associes)
RH:true:true:true:Consulte le plan de charges
Utilisateur::::Consulter le plan de charges.

Les acteurs et les droits: petite histoire d'elaboration. 

Ne pas mélanger les droits et les roles. 





# Concepts pas clair
nom:definition:exemple
CEO:Le patron de l’entreprise:Le CEO gere l’ensemble de l’entreprise
Plan de charge:Representation de la repartition des intervenants du projet repartition sur le temps NB - tous les plans de charge sont disponibles aux utilisateurs authentifies:Un chef de pr
ojet consulte le plan de charge




# Cela vous fatigue pas de vous répéter ?
1:Commerciaux:Consulter le plan de charges et les logs
9:RH:Consulter le plan de charges et les logs
5:CEO:Consulter le plan de charges et les logs

pas de copie coller -> Forax vous dit pas de copier coller !


# Les préconditions doivent être liés a des cas d'utilisation.
 
        --## Preconditions

        Il faut que :
        - le plan de charge ait ete cree -> ou est le cas d'utilisation 
        - l'utilisateur soit authentifie -> ou est le cas d'utilisation 
        - l'utilisateur ait un acces a internet pour consulter le plan de charge


        -- ### Conditions de succes 
        Le plan de charge est affiche. 

# Ce n'est pas un déclencheur. 
    **Declencheur** : L'utilisateur selectionne l'action de modifier le/un ?  plan de charge (changer l'attribution d'un creneau a un utilisateur)<br/>



----------------------------
Un perimeter.md 

##      Fonctionnalite incluse dans le projet 

1. Liste des plat/pizza/boisson
2. Interface sur un terminal pour crée une commande 
3. Modélisation du restaurant avec les tables occupees/libres
4. Interface un terminal pour gestion des commandes
5. Affichage dans un terminal tiers des plats a préparer, triés en fonction du type et du responsable
6. Provision de terminaux sur lesquelle faire tourner l'application
7. Affichage d'un recapitulatif d'une commande l'instant T 
8. Affichage a la demande des commandes en fonction de leur états

##      Fonctionnalite non prise en compte part le projet

1. Gestion des stock, l'appli ne connait pas l'etat du stock lors de la commande d'un plat, elle ne les mets pas a jours non plus
2. L'application ne notifie pas les serveurs lorsqu'une commande est prete, le patron souhaite garder l'ancien systeme de clochette
3. L'application ne gére pas la compta elle se contente juste d'envoyer une facture (plat et prix) de ce qui a été commandé a un logiciel tiers (pizzacompta)
4. L'application ne propose que des fonctionnalitees en lien avec la prise de commande et dans le cadre d'un seul restaurant.


-------------------------
# Exercice identifier les acteurs suivant et le système envisagé 
X:True:True:True:Intéragit avec le système  <- rien 
X:True:True:True:Intéragit avec le système
X:True:True:True:Intéragit avec le système
X:False:True:True:Consultation d'informations via le système
X:False:True:True:Consultation d'informations via le système
X:False:False:False:Fournit le moyen de s'authentifier

-----------------------------
# Heureusement les acteurs sont décrit dans le glossaire 
# tient je pensai ils n'y apparaisait pas 
# bizarre 
+ plan de charge:Outils permettant de prévoir l'activité d'une équipe au fil du temps:Planning prévisionnel du mois de juin.
- intervenant:Personne/Ressource qui travaille sur un projet:Ingénieur
- commercial:Personne qui s'occupe de vendre les projets:Responsable des ventes
- chef de projet:Personne qui gère une équipe d'intervenants lors de la réalisation d'un projet:Le responsable du projet X
- LDAP:Système fournissant une API permettant l'authentification des utilisateurs:Le serveur de la société qui contient la base de données des utilisateurs
- API:(Application Progamming Interface)Interface permettant de dialoguer avec un système externe:L'API de la société qui fournit les comptes utilisateurs
+ projet:Un ensemble finalisé d’activités et d’actions entreprises par une « équipe projet » sous la responsabilité d'un chef de projet dans le but de répondre à un besoin défini par un contrat dans des délais fixés et dans la limite d'une enveloppe budgétaire allouée:Construction d'un bâtiment

Un projet dans l'entreprise visé: un ensemble de triplets (periode,personne), le projet a défini comme un période: 

matrice compétence: donc c'est personne,compétence, niveau d'exertise, niveau d'interet

période:un interval de dates: Le projet doit être fini avant fin aout


+ compétence:aptitude d'un intervenant à réaliser une tâche:Peut développer une interface web
+ souhait d'un intervenant:Intérêt d'un utilisateur pour un projet donné:Je ne veux pas bosser pour Marlboro


# je comprend pas !
plan de charge:Outils permettant de prévoir l'activité d'une équipe au fil du temps


-----------------
# J'aime :
-> un cas d'utilisation pour entrer les compétences 

-> des cas d'utilisation sur la bonne voie j'aime les alternatives/erreurs 

++++++++++++++++++++++

# Use case 28 !

10:Etre alerté budget:chef de projet:10:login, si un budget d'un projet du chef de projet dépasse le budget alloué, le chef de projet voit une notification sur la page d'accueil, il clic dessus et est redirigé vers la page du projet correspondant, il peut constater le dépassement du budget.

si j'ai bien compris c'est lui qui fait les affectations a son projet ? 
sinon je pense qu'il souhaite recevoir un mail si quelqu'un lui prend/affecte du personnel ce qui modifie son enveloppe ....


11:Saisir projet:chef de projet:11:login, le chef de projet clic sur l'onglet ""projets"" il voit un tableau répertoriant les projets du mois en cours, il clic sur un projet, il peut renseigner les champs de descriptions du projet (nom, dates de débuts/fin, budget ...)"

j'ai un peu de mal a comprendre c'est le chef de projet qui s'affecte des projets ?

++++++++++++++++++

# Pré-requis 
    l'utilisateur est identifié 
    l'utilisateur a les droits d'affectation d'une ressource à un projet
# Déclencheur doit disponible dans un autre cas d'utilisation 
    l'utilisateur a selectionner l'onglet intervenant 

## Scenario Nominal

2. l'utilisateur choisi un intervenant  
3. Le système construit et affiche le tableau récapitulatif des missions de l'intervenant. 
4. et le système affiche sur une "ligne temporelle" le pourcentage d'occupation de l'intervenant par rapport à ses disponibilité pendant le mois en cours.
5. Le chef d'entreprise clic sur la date du jour et peut sélectionner dans le calendrier qui s'affiche une date jusqu'à laquelle il souhaite voir les prévisions du plan de charge.

6. L'<<acteur>>> principal du cas d'utilisation a réalisé son objectif a savoir <<blabla>>




+++++++++++++++++++++++

## acteurs 

Les noms des acteurs sont trop compliqués il faut un seul mot.

Planificateur, Ressource, drh, annuaire.

Pensez vous que le 'Demandeur du projet/boss/directeur technique' doit accèder comme le 'Chefs de projet/ingénieurs' au plan de charge.


++++++++++++
## Usecase 

Bon ok mais j'ai pas vu la définition de valider ni le workflot.

1.          Accepter un nouveau projet
2.          Saisir son nom, son demandeur et le nombre d'heures de travail prévisionnelles dans l'application
3.      Enregistrer et/ou Valider (Mais enregistre pour pas perdre les valeurs)

============


## glossaire 
- intervenant/ressource:Un membre de l'équipe technique:Ingénieurs, apprentis, stagiaires sont des intervenants
- ressource:Une ressource est un intervenant:Ingénieurs, apprentis, stagiaires sont des ressources
+ disponibilité:Quantité de temps non réservée à une activité précise:Le nombre de jours hommes non réservés d'un intervenant sur une période de temps donnée (un jour, une semaine, un mois)

IL faut vous décider intervenant ou ressource ?


==============
## Scenario Nominal

1.      L'intervenant se connecte sur l'application.
2.      L'intervenant indique la période voulue de consultation via un calendrier.
3.      Le système calcule la charge de chaque intervenant sur chaque projet de chaque client.
4.      Le système envoie et affiche le résultat.
5.      l'intervant a obtenue l'information souhaité (objectif)

Beaucoup de choses a dire ....

%%%%%%%%%%%%%%%%%%

Boss:True:True:False:Acces en lecture a l'application
Chefs de projet:True:True:True:Interragi avec l'application
Les commerciaux:False:True:False:Accès a l'application
Directrice des ressources humaines:False:True:False:Acces en lecture a l'application
Directeur technique:True:True:True:Interragi avec l'application
Les ingenieurs:True:True:True:Interragi avec l'application
Annuaire:True:False:False:Fournir les identifiants


