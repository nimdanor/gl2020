# Cas d'utilisation N° {{nbuc}} :  Etudiant

Niveau {{order}}

##	Description

Consulter le temps d'attente estimé pour pouvoir se restaurer

_[L'etudiant veut connaître le temps d'attente dans la file du CROUS, il doit consulter l'écran d'affichage]_   
 **[{{concept}}](https://github.com/nimdanor/gl2020/new/master/tp2/groupe7/sujet7_2/UC/Etudiants/{{etudiant}}.md)**  

> **Niveau** : Objectif utilisateur 
> **Déclencheur** : C'est l'heure du déjeuner (l'étudiant veut se restaurer rapidement pour retourner en cours à temps)
> **Acteur Primaire**: Etudiant   
> **Acteurs secondaires**:   
> **Parties Prenantes concernées** : Ecran
 
 
## Preconditions

1. Jour d'ouverture de l'école, période scolaire et en semaine
2. Arriver de la pause déjeuner

## Scenario Nominal

1.	L'etudiant se rend devant le restaurant du CROUS  
2.	Il consulte le temps d'attente dans la file du restaurant via les écrans
3.	Le temps lui paraît convenable il entre dans la file d'attente  
4.	Le temps estimé est écoulé, c'est au tour de l'étudiant
5. L'étudiant se restaure

###	Extensions

3. Le temps d'attente semble inconvenable
4. L'étudiant trouve un autre moyen de se restaurer
5. L'étudiant se restaure

## Post Conditions
### Conditions de succès 

Temps d'attente éstimé correct, à 3 minutes prêt, l'étudiant a eu le temps de se restaurer sans arriver en retard à son prochain cour

### Minimal Guarantees

Fournir une estimation du temps d'attente en fonction du nombre d'étudiants dans la file et le restaurant.

### Conditions final en cas d'échec

Le sytème a averti l'étudiant qu'il n'aurait pas le temps de se restaurer au CROUS, l'étudiant a pu se débrouiller autrement.


### Frequence

Ce cas d'utilisation apparaît tous les jours d'ouverture du restaurant et pour chaque étudiant qui souhaite s'y restaurer.

### Besoins Spéciaux (optionel)  


### Performance  
###	Security  
###	Usability / Accessibility  
Ecrans d'affichage disponibles dans tout le hall
###	Other  

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
