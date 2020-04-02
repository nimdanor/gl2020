# Cas d'utilisation N° {{nbuc}} :  Consultation de la queue

Niveau __Objectif utilisateur__

## Description

Un salarié du CROUS doit pouvoir consulter l'état de la file d'attente afin de pouvoir 
anticiper les besoins en nourriture en conséquence.

FIXME N'oubliez pas de mentionner le concept **[{{concept}}](https://github.com/PremierLangage/plconception/blob/master/conception/concept/{{concept}}.md)**  

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : _[Describe the event that initiates the use case.]_ TODO  
> **Acteur Primaire**: Utilisateur   
> **Acteurs secondaires**: TODO   
> **Parties Prenantes concernées** : TODO   
 
 
## Preconditions

Le système doit être capable de détecter la quantité d'élèves en train de faire la queue, et d'afficher cette
information sur un écran visible par les salariés du CROUS.


## Scenario Nominal

1.	Les élèves font la queue
2.	Le système analyse la queue via la caméra
3.	Le système affiche sur un écran visible par les salariés CROUS le nombre d'élèves en train de faire la queue
4.	Le salarié CROUS prépare les quantités de nourriture en conséquence

###	Extensions

Si le système n'arrive pas à analyser la queue (2) ou que l'affichage ne fonctionne pas (3), alors le salarié CROUS 
doit faire confiance à son instinct de professionnel de la restauration.

## Post Conditions
### Conditions de succès 

Le salarié arrive à estimer précisemment la quantité de nourriture nécessaire, ce qui évite le gachis. 

### Minimal Guarantees
FIXME _[Describe the guarantee or assurance that this Use Case provides to all Actors and Stakeholders to protect their interest regardless of whether the Use Case ends with success or failure.]_

### Conditions final en cas d'échec

Il y a un gachis de nourriture.


FIXME _les variables suivantes sont optionnelles._

### Frequence

Ce cas d'utilisation aura lieu à tous les repas du midi.

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
