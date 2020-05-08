  
# Modalités de Rendu  pour la deuxième interview   
  
  
En binome.  
  
Pour vérifier votre archive vous avec le fichier verifcsv.py, placer votre archive + verifcsv.py dans un nouveau répertoire pour tester.   
  
Dans une archive **mashupofstudentnames.zip** d'un répertoire mashupofstudentnames qui contient les fichiers suivants:  
  
  
  
Le diocument technique pour vous identifier et aider les outils automatiques:  
  
0) **student.json**     
  
> **Attention** ajout du email.  
  
```  
{"binomes":[{"nom":"Durand","prénom":"Jacques","etudiant":10567,"email":"jd@etud-univ-eiffel.gustave.fr"},{"nom":"Duplan","prénom":"Paulette","etudiant":42, "dp@etud-univ-eiffel.gustave.fr"}],  
"repertoire":"machupofstudentnames","sujet":XXXXX}  
```  
**Attention** au sujet :    
XXXXX = "pizzaza" ou "plan de charge"  
  
  
  
1) **readme.md** de présentation de votre travail.  
  
Effectivement nous ne fournirons pas les documents suivants au client mais nous les utiliserons pour lui faire une réponse.  
Présenter le logiciel visé en quelques lignes. Vous pouvez vous inspirez du perimtrètre mais ce n'est pas identique.
Parler nous de ce qui est IMPORTANT pour le client et pourquoi cela répondra au besoin.


  
2) Dans un fichier **acteur.csv** fournir une liste des acteurs avec les colones suivantes :  
```  
nom:principal:humain:formation:role  
```  
Où nom et role sont des strings et principal, formation, humain sont des booleens True et False (avec toutes les case autorisés).  
exemple:  
```  
client:True:True:FalsE:Réalise des operation banquaire sur le distributeur  
```  
  
3) Dans un fichier **objectif.csv** fournir une liste des objectif de chaque acteurs.  
```  
num:acteur:objectif    
1:client:Retirer de l'argent d'un compte sous forme de billets    
2:client:Connaitre le solde d'un de ses comptes     
3:operateur:Connaitre a distance le niveau des fournitures billets, papier    
4:directeur:Visualiser les plages d'utilisation hebdomadaire du DAB    
```  
  
4) Dans un fichier **usecase.csv**   
```  
num:name:acteur:objectif:resume     
1:Retirer Argent:client:1:le client entre sa carte,le système vérifie l'identité, le client choisi le montant, le système créér la transaction banquaire de soustraction du montant, la banque valide la transaction, le distributeur rend la carte, le distributeur fournis le papier, le distributeur fournis les billets correspondant au montant.     
2:Connaitre Solde:client:2:le client entre sa carte,le système vérifie l'identité, le client choisi afficher solde, le système rend la carte, le système récupère et imprime le solde,      
```  
5) Cas d'utilisation, pour les 4 premiers cas d'utilisation.    

Les fichiers suivants:    
   **usecase1.md**    **usecase2.md**   **usecase3.md**    **usecase4.md**    
Contenu :  
https://github.com/nimdanor/gl2020/blob/master/tp2/template.txt  
  
  
6) Dans un fichier **concept.csv** fournir une liste de concepts le glossaire   
Avec definition est la definition en intension (sens) et exemple est une défintion en extension ou vous donner un exemple de l'usage du concept.  
```  
nom:definition:exemple  
dab:machine physique qui permet de réaliser des opérations banquaire en autonomie:Un écran clavier lecteur de carte distriuteur_de_billet et mini imprimante   
reçu:Document papier fournis par le dab:Solde,transaction,echec,  plusieurs cas de figure.  
```  
  
7) Dans des fichiers *.pulm les scémas uml suivant. 
> **acteur.plum** diagramme des acteurs (héritage entre acteurs).  
> **usecase.plum** diagramme des cas d'utilisation (lien entre les acteurs et les cas d'utilisation).


