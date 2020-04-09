# Cas d'utilisation N° 01 :  Consultation de la File d'Attente

##	Description

Les consommateurs peuvent consulter l'état de la file d'attente lorsqu'ils souhaitent se rendre au CROUS pendant la pause midi / le soir.

> * **Déclencheur** : C'est l'heure de la pause pour manger
> * **Acteur Primaire**: Consommateur   
> * **Acteurs secondaires**: Employés du CROUS
> * **Parties Prenantes concernées** : Caméras
 
## Preconditions

* Les dispositifs de détection sont activés
* La pause à commencée
* La cantine n'est pas fermée

## Scenario Nominal

FIXME_[tout ce passe bien c'est le scénario parfait .]_

1.	L'utilisateur lance l'application
2.  L'utilisateur choisit quel restaurant vérifier

###	Extensions
FIXME Moins bien _[Document alternate flows and exceptions to the main success scenario. Extensions are branches from the main scenario, and numbering should align with the step of the success scenario where the branch occurs.]_

FIXME Indiquez dans quel point du scenario nominal le chemin alternatif démarre et ou il reprend.


## Post Conditions
### Conditions de succès 
Le/la secrétaire peut récupérer les notes d'un groupe / classe sous forme affichable directement (par exemple, tableau excel), ainsi que les calculs statistiques qui accompagnent les notes :

* Moyenne
* Médiane
* Ecart-type
* Classement

### Minimal Guarantees
Dans tous les cas, les notes doivent être récupérées, avec les différents critères et les apprentis associés.

### Conditions final en cas d'échec
En cas d'échec, les notes sont perdues ou déréférencées par rapport aux apprentis.

FIXME _les variables suivantes sont optionnelles._


### Frequence
A chaque fois qu'il y a une session de soutenances.

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
