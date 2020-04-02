# Cas d'utilisation N° {{nbuc}} :  Envoie_flux_vidéo 

Niveau Haut niveau

##	Description

{{comment}}

La caméra doit envoyer sont flux vidéo au system pour analyse. 
FIXME N'oubliez pas de mensioner le concept **[{{concept}}](https://github.com/PremierLangage/plconception/blob/master/conception/concept/{{concept}}.md)**  

> **Niveau** : Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : Entrer dans la plage horaire de fonctionnement du CROUS  
> **Acteur Primaire**: Caméra   
> **Acteurs secondaires**: Systeme, Ecran   
> **Parties Prenantes concernées** : CROUS, CRI   
 
 
## Preconditions

La caméra doit etre branché et enregistrer dans le systeme avec droit d'envoie de fichier.


## Scenario Nominal

1.	La caméra se connecte au systeme
2.	La caméra filme l'entrée/sortie du batiment
3.	Toute les minutes elle envoi ce qu'elle à filmer au systeme

###	Extensions

1.	La caméra se connecte au systeme
  1.1 La camera n'arrive pas a se connecter
  1.2 Elle ré-essaye 3 fois attend 5mn ré-essaye 3
  1.3 Si toujours pas de connection, ouverture d'un ticket 
2.	La caméra filme l'entrée/sortie du batiment
  2.1 La camera ne filme pas
  2.2 ouverture ticket 
3.	Toute les minutes elle envoi ce qu'elle à filmer au systeme
  3.1 connexion lente et ou instable
  3.2 Toute 5m envoie une minute 

## Post Conditions

### Conditions de succès 
Les fichiers sont transmis en continue dans le systeme

### Minimal Guarantees
Au moins un fichier d'une minute est present toutes les 5 minute

### Conditions final en cas d'échec
Un ticket d'ecrivant l'erreur a été envoyé au CRI

FIXME _les variables suivantes sont optionnelles._

### Frequence
Plusieur fois par jour 

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
