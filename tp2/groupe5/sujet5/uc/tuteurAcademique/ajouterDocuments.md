

# Cas d'utilisation N° 5 :  Remplir document de suivi

Niveau objectif utilisateur

##	Description
- Remplir/upload les documents de suivi (ex: fiche académique de l'étudiant)

> **Niveau** : Objectif utilisateur   
> **Déclencheur** : Cliquer sur l'onglet "Documents a remplir" 
> **Acteur Primaire**: Tuteur académique   
> **Acteurs secondaires**: TODO   
> **Parties Prenantes concernées** : TODO   
 
 
## Preconditions
1.	L'enseignant se logge sur la plateforme
2.	Il selectionne l'étudiant cible dans la liste de ces étudiants
3.	Il est sur la page "Suivi académique"
4.  Clique sur "Document a remplir"
5.	Acceder à la liste des documents a remplirs


## Scenario Nominal

1.	L'enseignant se logge sur la plateforme
2.	Il selectionne l'étudiant cible dans la liste de ces étudiants
3.	Il clique sur l'onglet "Suivi"
4.	Il clique sur l'onglet "Documents à remplir"
5.  CLique sur un document
6.  Remplir / uploader le document  
7.  Clique sur "enregistrer"

###	Extensions

## Post Conditions

### Conditions de succès 
- Modification sur le document enrégistrer 
- Mise a jour du document
- Notification à l'étudiant que le document en attente a été rempli

### Minimal Guarantees
- Avoir une sauvegarde des documents
- Sauvegarde partiel du document (à l'instant T)
- Pourvoir reprendre le document dans l'état de la dernière compétence

### Conditions final en cas d'échec
- Afficher un message pour indiquer si le sauvegarde a été un success ou pas 
  
### Frequence

### Besoins Spéciaux (optionel)  

### Performance  

###	Security  

###	Usability / Accessibility  

###	Other  
- Limite la taille du fichier à uploader (TODO: Définir cette taille limite)
- Utiliser des formats standard (pdf, doc, txt)

##	Problèmes et étapes suivantes  
