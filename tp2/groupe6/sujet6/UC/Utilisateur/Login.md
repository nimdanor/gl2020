# Cas d'utilisation N° 01 :  Authentification

##	Description

Avant de pouvoir accéder aux fonctionnalités, il faut se connecter. L'accès aux fonctionnalités est bloqué pour toute personne qui n'est pas connecté.

> **Niveau** : ? 
> **Déclencheur** : Un utilisateur non connecté affiche la page de connexion ou essaye d'accèder à une fonctionnalité.
> **Acteur Primaire**: Utilisateur, LDAP 
> **Acteurs secondaires**: None
> **Parties Prenantes concernées** : None 

___
 
 
## Preconditions

L'utilisateur n'est pas encore connecté.

___


## Scenario Nominal

1.	L'utilisateur accède à la page de connexion
2.	L'utilisateur envoie ses identifiants
3.	Le système reconnaît les identifiants
4.	Le système affiche que la connexion s'est bien effectué

###	Extensions
#### Mauvais identifiants

1. L'utilisateur accède à la page de connexion
2. L'utilisateur envoie ses identifiants
3. Le système ne reconnaît pas les identifiants
4. Le système affiche que la connexion ne s'est pas bien passée
5. Retour à la page de connexion

___


## Post Conditions
### Conditions de succès 
Si l'authentification réussie, l'utilisateur est connecté.

### Minimal Guarantees
La page de connexion est disponible pour les utilisateurs non connectés. 

### Conditions final en cas d'échec
En cas d'échec, un utilisateur ne doit pas être connecté.

### Frequence
FIXME _[Indicate how often the use case is expected to occur. This information aids designers and developers in understanding capacity requirements.]_   
### Besoins Spéciaux (optionel)  
FIXME _[Describe any additional factors that impact the execution of the use case. These could be environmental, regulatory, organizational or market-driven in nature.]_  
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
