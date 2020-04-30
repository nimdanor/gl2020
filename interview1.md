
# Modalités de Rendu 

En binome.


Dans une archive **machupofstudentnames.zip** d'un répertoire machupofstudentnames qui contient les fichiers suivants:

0) **student.json**
```
{"binomes":[{"nom":"Durand","prénom":"Jacques","etudiant":10567},{"nom":"Duplan","prénom":"Paulette","etudiant":42}],
"repertoire":"machupofstudentnames"}
```

1) dans un fichier **acteurs.csv** fournir une liste des acteurs avec les colones suivantes :

nom:principal:humain:formation:role

Où nom et role sont des strings et principal, formation, humain sont des booleens python True et False 
exemple:

client:True:True:False:Interragi avec le distributeur.

2) Dans un fichier **Objectifs.csv** fournir une liste des objectif de chaque acteurs.

num:acteur:objectif  
1:client:Retirer de l'argent d'un compte sous forme de billets  
2:client:Connaitre le solde d'un de ses comptes   
3:operateur:Connaitre a distance le niveau des fournitures billets, papier  
4:directeur:Visualiser les plages d'utilisation hebdomadaire du DAB  

3) Dans un fichier **concept.csv** fournir une liste de concepts le glossaire 
Avec definition est la definition en intension (sens) et exemple est une défintion en extension ou vous donner un exemple de l'usage du concept.

nom:definition:exemple
dab:machine physique qui permet de réaliser des opérations banquaire en autonomie:Un écran clavier lecteur de carte distriuteur_de_billet et mini imprimante 
reçu:Document papier fournis par le dab:Solde,transaction,echec,  plusieurs cas de figure.


4) dans un fichier **usecase.csv** 

num:name:acteur:objectif:résumé   
1:Retirer Argent:client:1:le client entre sa carte,le système vérifie l'identité, le client choisi le montant, le système créér la transaction banquaire de soustraction du montant, la banque valide la transaction, le distributeur rend la carte, le distributeur fournis le papier, le distributeur fournis les billets correspondant au montant.   
2:Connaitre Solde:client:2:le client entre sa carte,le système vérifie l'identité, le client choisi afficher solde, le système rend la carte, le système récupère et imprime le solde,    

5) Cas d'utilisation, pour les 4 premiers cas d'utilisatio.  
Les fichiers suivants:  
**usecase1.md**  
**usecase2.md** 
**usecase3.md**  
**usecase4.md**  
Contenu :
https://github.com/nimdanor/gl2020/blob/master/tp2/template.txt


6) Périmètre / MOD 
 **perimeter.md** 
 **MOD.png** ou **MOD.svg** ou **MOD.jpg** 

