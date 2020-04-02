
# Cas d'utilisation N° 08 :  Traiter les notes

##	Description

Affichage et calculs statistiques sur les notes déjà entrées par l'évaluateur. Le secrétaire doit pouvoir récupérer les notes et les avoir automatiquement sous une forme partageable :
* Pour les apprentis : Note personnelle multicritériée, classement.
* Pour les enseignants : Ensemble des notes multicritériées sous forme d'un tableau avec calculs statistiques le cas échéant.

> * **Déclencheur** : Les soutenances sont terminées, il faut traiter et partager les notes.
> * **Acteur Primaire**: Secrétaire   
> * **Acteurs secondaires**: Evaluateur, Enseignant, Apprenti 
> * **Parties Prenantes concernées** : Jury  
 
## Preconditions

* Soutenances terminées
* Notes saisies par les évaluateurs

## Scenario Nominal

FIXME_[tout ce passe bien c'est le scénario parfait .]_

1.	Les soutenances sont terminées et les notes ont été saisies.
2.	Le.a secrétaire récupère l'ensemble des notes.
3.	Le.a secrétaire saisi le type d'informations nécessaires (par exemple la moyenne)
4.	Le.a secrétaire récupère les informations.
5. Le.a secrétaire récupère les informations sous forme d'un tableau qui contient les informations sur les notes et les apprentis.

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
