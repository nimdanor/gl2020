# Cas d'utilisation N° 1 :  Gestion des données des cartes

- Niveau Objectif Utilisateur

##	Description

- Le gestionnaire de données est responsable de l'import de nouvelles données qui seront ensuite affichées sur les cartes.
- Il est également responsable de la vérification de l'intégrité de ces dernières en les mettant à jour et en les supprimant dans certains cas.

> **Niveau** : Objectif utilisateur
> **Déclencheur** : Besoin d'ajout/de moficiation d'une donnée 
> **Acteur Primaire**: Gestionnaire   
> **Acteurs secondaires**: -
> **Parties Prenantes concernées** : -
  
## Preconditions

- Le gestionnaire doit avoir à sa disposition une interface permettant d'insérer des données provenant de sources externes (BDD).
- Il a également besoin d'une interface lui permettant de modifier les données intégrées au système.

## Scenario Nominal

1.	Connexion à l'interface d'administration
2.	Ouverture du panel d'insertion d'une nouvelle donnée
3.	Insertion des informations concernant la nouvelle donnée
4.	Validation de l'insertion
5.  Ouverture du panel de modification des donnnées
6.  Sélection d'une donnée existante
7.  Modification des informations concernant la donnée sélectionnée
8.  Validation des modifications
9.  Ouverture du panel de suppression des données
10. Sélection d'une donnée existante
11. Validation de la suppression de la donnée

###	Extensions

- 

## Post Conditions
### Conditions de succès 

- Les modifications effectuées doivent apparaître au sein du système une fois la validation effectuée.

### Minimal Guarantees

-

### Conditions final en cas d'échec

-

### Frequence

- Faible

### Besoins Spéciaux (optionel)  

- 

### Performance  

- 

###	Security  

-

###	Usability / Accessibility  

-

###	Other  

-

##	Problèmes et étapes suivantes  

-
