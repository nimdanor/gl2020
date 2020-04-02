# Cas d'utilisation N° 1 :  Expression des voeux

Niveau Objectif utilisateur

##	Description

L'enseignant exprime ses voeux d'enseignement (choix de modules, format) 
L'enseignant doit cumuler un nombre minimum de 192H de cours. 

> **Niveau** : Objectif utilisateur 
> **Déclencheur** : TODO  
> **Acteur Primaire**: Enseignant   
> **Acteurs secondaires**: Responsable de filière   
> **Parties Prenantes concernées** : Etudiants  
 
 
## Preconditions

L'enseignant doit avoir accès au système. 
La liste prévisionnelle des enseignements doit être effectuée. 
La liste des intervenants doit être à jour. 

## Scenario Nominal

1.	L'enseignant se connecte à l'interface.  
2.	L'enseignant choisit un cours.
3.	L'enseignant chosit un / plusieurs format.
4. L'enseignant valide ses voeux. 
5. L'enseignant se déconnecte.  

###	Extensions
FIXME Moins bien _[Document alternate flows and exceptions to the main success scenario. Extensions are branches from the main scenario, and numbering should align with the step of the success scenario where the branch occurs.]_
FIXME Indiquez dans quel point du scenario nominal le chemin alternatif démarre et ou il reprend.
Lors de la validation (étape 4), l'enseignant n'a pas renseginé sont objectif de 192h de cours. 
L'enseignant est renvoyé à l'étape 2 pour choisir un cours.


## Post Conditions
### Conditions de succès 
L'enseignant valide ses voeux avec un minimum de 192h de cours. 

### Minimal Guarantees
Les voeux de l'enseignant seront enregistrés dans la bdd. 

### Conditions final en cas d'échec
L'enseignant ne renseigne pas 192h de cours. 

FIXME _les variables suivantes sont optionnelles._

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
