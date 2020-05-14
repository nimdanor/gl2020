
Retour généraux sur le DM2


Le point le plus important :

Un cas d'utilisation 

Document naratif --> ça raconte une histoire 
le dialogue entre l'acteur et système --> 
    Acteur: bla bla 
    Système: blabla 
    Acteur: Blabal 
Un dialogue -> une suite d'**évènements** IHM ou API 

    
Comment il fait pour atteindre son objectif en utilisant le système.


Serveur -> authentifié => login -> identifiants => administration --> déployement du logiciel il faut crée un administateur --> documentation => au moment déployement 
on doit créer cet administration admin/admin 


Login 
1. Le système propose une interface de connection.
2. l'utilisateur saisie login et mot passe.
3. le système vérifie que le couple login/motpass existe et valide et autrhisé 
    le système lance la procedure de connection et affiche le menu d'acceuil.
4. l'objectif de l'utilisateur est atteint : être connecté. 

Alternatif:
3. le couple login motdepass n'est pas reconnu.
   le système affiche un message d'erreur et retourne en 1.




Création d'une commande:
1. le système affiche le menu 
2. le serveur choisi le menu création commande 
3. le système affiche le formulaire de création de commande 
4. le serveur choisi la table,  indique le nombre de couvert
5. le système enregistre la table et le nombre de couvert.
5.5  le système affiche l'interface de selection des Elements
6. le serveur :
    6.1 - choisir la catégorie de l'élement (plats/boissons/pizza/entrées/dessert)
    6.2 - le système affiche la catégorie eventuellement de façon recursive la sous catégorie.
    6.3 choisi un element boucler en 5.5
   le serveur choisi la fin de la commande. 
7. le système affiche un récapitulatif.
8. le serveur valide le récapitulatif 
9. le système envois aux préprateur correpondant les elements à préparer. 

Elements: une chose a préparer et a servir : plats/boissons/pizza/entrées/dessert.
menu: une structure de donnée qui contient tout les éléments.











acteur.csv je fait le test les premières lignes doivent avoir principal==True  
OUTIL important les données : comment font elles pour arrivre dans le logiciel


AgulloMarti

    Acteurs ok Dessin acteur ok (mais bof non ?)

    j'aime pas l'ordre d'importance des acteurs. 
    
    Le truc dur c'est la prise de commande cela doit être en premier.

    bizarre --> Allumer les écrans et charger l'affichage correspondant
    bulbizare --> L'application enverra les données à l'écran du comptable.
    Ronflex --> Recevoir un advertissement sonore pour le besoin imminent d'une préparation

    Scénario nominal du serveur : inadéqua !

    Pas de saisie du nombre de clients.
    Pas de saisie du numéro de table. 
    Pas d'explication sur le controle de la commande.

    Globalement 11/20

Nicolas Baticle / Altan XX
    plan de charge

    Trop d'acteurs, ici il faut piloter avec les droits, ce que vous n'avez pas fait qui dit que je suis un commercial ou le CEO cette donnée arrive comment dans votre logiciel.--> donnée importante de votre logiciel. 
    
   
    Comment je fait pour savoir quels sont les projets de l'utilisateur.

    c'est quoi une statistique ??? c'est pas dans le glossaire.

    c'est quoi une charge, une tâche, 

    je voudrais bien avoir "":Avoir des informations sur les statistiques d’un projet""
    mais c'est très vague dans votre desciption j'aurais aimer quelque chose qui mde dise ce que je vais voir sur le écran.

    Le diagramme des cas d'utilisation n'est pas efficace.
    le glossaire est insuffissant.

    Globalement je ne comprend pas ce que fait le logiciel a part qu'il gère une plan de charge mais sans savoir ce qu'est un plan de charge.

    Globalement: 6/20 

Bourjot-Durand
    plan de charge

    Trop d'acteurs, ici il faut piloter avec les droits, ce que vous n'avez pas fait qui di que je suis uun comercial ou le CEO cette donnée arrive comment dans votre logiciel.

    Votre dessin  UML des acteurs est étrange il n'y pas des liens d'héritage qui sont les seul autorisés entre acteurs et le sens des fleches est étonnant.
    
    Concepts pas mal.
    
    J'ai peur que le **perimetre.md** vous ai manqué, car un certain nombre de chose semble hors périmètre dans vos cas d'utilisation. Mais c'est un moindre mal vous n'avez que perdu un peu de temps, beaucoup moins que si vous aviez oublier quelque chose.

    
    usecase1 que fait le système ??
    usecase2 idem ??
    ...
    C'est quoi un cas d'utilisation ?? 
    un dialogue !
    

    Globalement: 8/20   grace au glossaire 



diasoliveiradescombes/

    Acteurs pourquoi un barista et pas un pizaiolo  ?
    ET sinon pourquoi différentier le barman du cuistot ?
    Qu'est ce qui différentie les deux roles ??
    
    Glossaire vous vous fatiguer a definir plat/entré/dessert/boisson etc 
    et puis vous ne les utiliser pas pour définir une commande ! 
    bizarre non ?
    
    J'aime toujours pas les objectifs des acteurs non humains. Définissez une partie prenante qui vas avoir besoin de l'information. 

    Vous avez mis des liens entre cas d'utilisation je pense que toutes les flèches sont fausses.
    Vous pouvez mettre une dépendance entre creationcommande et ajouterboisson mais pas un include !
    
    usecase1 P....! ce use case n'a pas d'interet! metter en premier le cas d'utilisation important 
    usecase2 que fait le système ?? je comprend pas
        **UN PREREQUIS C'EST UN CAS D'UTILISATION QUI A LIEUX AVANT**
    usecase COPY/PASTE beurk 
    usecase4 Bof, pas de controle de la commande le système ne fait rien
    
    globalement: 7 /20


Cau_Traina/

    Acteur on commence par le 
    patron:False:True:True:Patron de l'entreprise. Son objectif est de la gérer.
    7:patron:Récupérer les statistiques du restaurant.
    Dommage statistique n'est pas définie donc pas d'interet.
    dessin raté

    glossaire 
    j'aime "vague" 
    j'aime pas commande:Une commande est un séquence de plats demandés par une table 
    un seul client par table ?? 
    c'est pas ce que l'on avait dit.

    objectifs
    3:serveur:Servir un plat à une table ?? entendre la cloche

    usecases
    ordre OK
    je suis pas encore conviencu de faire passer la communication du fait que les plats soit près par l'application 
    dessin -> bizare 
    
    OK pour un cas d'utilisation presque raisonnable pour prendre la commande 
    
    
    globalement : 12 (sauvé par le scénario nominal)
    
    


koffinguyen-gl-dm2

    Beaucoup d'acteurs avec des roles effectifs,
    je ne sais pas si ils sont tous utiles pour la conception.
    principal n'est pas un acteur !!
    NE détournez pas la signification des outils cela vous met en danger.
    
    pourquoi répéter l'objectif d'authentification alors que vous avez un "utilisateur"
    
    useacse 
    pas mal

    useacseX moyens tirant sur le bof voyez vous même 
    Pourquoi le système ne fait rien dans vos cas d'utilisation

    globalement: 9 



LemoineDindane

    j'ai corrigé mais la prochaine fois les formats pas vérifiés -> 0 

    acteurs ok
    diagramme ok
    
    objectifs ok
    
    glossaire Excellent
    
    usecase ok
        ne pas privélégier le login comme use case 1 
    usecaseX peut mieux faire 
        vos préconditions ne sont pas bonne 

    Pour un début c'est pas mal !!
    
    globalement: 16 

machupofbessodesmartin

    acteurs ok mais ...
    
    je suis pas conveincu par le glossaire:
        -> copié collé du dico 
        -> pas de description de la notion de plan de charge 

    Mais alors pas convencu par les objectifs 
    
    Liste de usecase indigne 
    
    Les cas d'utilisation n'indique pas ce que fait le système ...
    

    globalement 4/20


MECHOUKOUZIEL 

    Acteur ok
    dessin acteur ok

    glossaire OK !

    objectifs 
        Ok
    liste usecase OK
    
    Les cas d'utilisation n'indique pas ce que fait le système ...
    précondition ok 


    globalement 16 



planChargeFallBohl

    acteurs 
    Chef : Il se doit de connaitre les compétences des ingénieurs ??
    pas d'héritage multiple en UML entre les acteurs 
    
    glossaire bien
    
    j'ai du mal avec l'objectif du commercial 
    8;Commercial;Définie le temps nécessaire à la réalisation d'un projet en fonction de la disponibilité des employés

    usecases liste ok

    pas très clair ce qui est echangé entre le système et les acteurs
    
    globalement 08


WINCKLER_JOLIVET
    pizzza
    
    acteurs ok (un peu trop peut être barman/cuisot/pizzaiola --> preparateur)
    
    Concept commence par des acteurs C'EST MAL !


    objectifs 
    Trois fois le même objectif : lire les préparations
    
    
    
    usecase 
    Les cas d'utilisation n'indique pas ce que fait le système ...
    précondition ok 
    je me marre (avec la voie de coluche):
    A l’étape 4, la commande n’est pas validée, le serveur ne peut pas achever le use case. Il reste à l’étape 4.

    Vous faites toujours les rigolo comme cela ?
    
    globalement 8

smerchernfau1
    pizza
    
    acteurs oui  (un peu trop peut être barman/cuisot/pizzaiola)
    plum =  zéro 
    puml
    
    glossaire
        commande peut mieux faire 
    
    le patron a changé de nom maitenant c'est le boss et comme c'est le boss on lui donne le cas d'utilisation numéro un dont on a pas parlé.
    
    Les cas d'utilisation n'indique pas ce que fait le système ...
    pas de description de la prise de commande 
    pas de prérequis clairs
    
    globalement 8

OUCH_PERNET

    acteurs 
    pas d'héritage multiple vers des acteurs que vous n'"avez pas définis 
    (voir schéma)

    Résultat on est noyé d'objectifs répétés 
    
    Référence d'un plat:La référence d'un plat est son nom en minuscule avec des tirets à la place des espaces.| nouilles_aux_fromage

    
    Les cas d'utilisation n'indique pas ce que fait le système ...
    "Le split des factures peut être problématique en fonction de l'implémentation."
    c'est très rassurant 
    Merci j'ai bien ri 
    
    globalement je sais pas quoi faire ... 



    
KHEROUA_QUANTIN
            
        Acteurs OK // dessin ok
        
        concepts
            commande rete le fait que le client peut être plusieurs personnes.
        
        objectifs OK
        
        usecase pas mal  très découpé 
            mais le cas d'utilisation principal n'est pas décrit 
        
        Les cas d'utilisations ne sont pas asser détailés.
        
        Globalement Très bien 18 


CRET-DACOSTA
    EVITER DE SORTIR DES FORMATS DEMANDES C'EST UNE EXIGENCE 
    ceci n'est pas le nom d'un acteur : "Serveur -> Consulteur, Serveur --> Enregistreur"
    ceci est indiqué dans le dessin et dans le texte de description de l'acteur (dont le contenu est libre).
    D'autre part il n'y a pas d'héritage multiple entre acteurs.
    
    concepts
        commande:"Une commande est composée d'un n° de table, éventuellement une entrée, un plat (avec les détails : ingrédients en plus/moins), éventuellement un dessert, le n° du serveur qui prend la commande, le nombre de client à la table et la date"
        OUI !
        
    objectifs
        moyen
    
    usecase
       liste pas mal 
    pas de dialogue

    Globalement 14

mathecowitschmarszal

    acteurs ok
    format inconnu pour les fichiers de dessin 
    je n'ai pas le logiciel
    
    concept
        plan de charge insuffisant 
    
    objectif
        commercial pas clair
        directeur technique je pense qu'il a des objectifs plusconcrets
    
    usecase 
        
    Ou est le système dans ce cas d'utilisation :
        1.      L'entreprise gagne un projet.
        2.      Un chef de projet est désigné.
        3.      Le chef de projet crée le projet dans l'application.


    globalement 9

jolivet_soustre 
    
        acteur ok
            Dessin acteur incorrect 
        concept
           pas d'acteurs s'il vous plait
        objectifs
        ok je ne comprend pas celui la 
            8:Gérant de pizzaza:Attribue ou réattribue les rôles du personnel

        usecases
            pas de dscription des interaction avec le système 
            le système fait des choses indirectement dans votre 
            description 
        
        
    globalement 9
