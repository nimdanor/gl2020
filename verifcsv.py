#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  verifcsv.py
#  
#  Copyright 2020 dominique Revuz <dominique.revuz@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import csv
import json
import zipfile 
import sys
import os

HEADERS={"acteur":["nom","principal","humain","formation","role"],
        "concept":["nom","definition","exemple"],
        "usecase":["num","name","acteur","objectif","resume"],
        "objectif":["num","acteur","objectif"],
        }


def build(repname):

    if not os.path.isdir(repname):
        os.mkdir(repname)
    if  not os.path.isdir(repname):
        print(" Votre système ne fonctionne pas !",file=sys.stderr)

    dico={"binomes":[{"nom":"Durand","prénom":"Jacques","etudiant":10567},{"nom":"Duplan","prénom":"Paulette","etudiant":42}]}

    with open(repname+"/student.json","w",encoding='utf-8') as f:
        json.dump(dico,f)
    
    for n,h in HEADERS.items():
        with open(repname+"/"+n+".csv","w",encoding='utf-8') as f:
            print(":".join(h),file=f)

    with open(repname+"/MOD.svg","w",encoding='utf-8') as f:
            print('<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"/>',file=f)



def loadstudent():
    return json.load(open("student.json","r"))


def createEmpty(filename, fieldnames, delimiter=":"):
    """
    >>> createEmpty("toto.csv", fieldnames= ['acteur', 'primaire'])
    >>> with open("toto.csv","r") as f:
    ...    print(f.readline().rstrip())
    acteur:primaire
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=delimiter)
        writer.writeheader()

def check(h,r):
    """
    Pourrait êter plus permissif en acceptant que r contiennent plus de clefs mais au moins les h. TODO 
    >>> check(["toto","titi"],{ "toto":3,"titi":4})
    True
    """
    s=set(h)
    v=set(r.keys())
    return s == v

def loadcsv(csvfile):
    """
    Creation de la liste des lignes 
    >>> loadcsv(open("kiki/acteur.csv","r"))
    [OrderedDict([('nom', 'kiki'), ('principal', 'True'), ('humain', 'False'), ('formation', 'False'), ('role', ' wag à tail')])]
    """
    try:
        s=csvfile.read(1024)
        if ":" in s:
            delimiter=":"
        elif ";" in s:
            delimiter = ";"
        csvfile.seek(0)
        reader = csv.DictReader(csvfile,delimiter=delimiter)
        return [row for row in reader]
    except Exception as e:
        print(s)
        print(e)
        return None

    
def verifcsv(csvfile,headers):
    """
    If there is no value in the file it is considered valide !!
    >>> with open("test.csv","w") as f:
    ...     print("acteur:primaire",file=f)
    ...     print("toto:False",file=f)
    >>> verifcsv(open("test.csv","r"), headers= ['acteur', 'primaire'])
    True
    >>> verifcsv(open("test.csv","r"), headers= ['acteur', 'secondaire'])
    False
    """
    s=csvfile.read(1024)
    if ":" in s:
        delimiter=":"
    elif ";" in s:
        delimiter = ";"
    csvfile.seek(0)
    reader = csv.DictReader(csvfile,delimiter=delimiter)
    for row in reader:
        if not check(headers,row):
            return False
    return True


filenamelist=["readme.md","acteur.csv","objectif.csv","concept.csv","usecase.csv","perimeter.md"]

def main(args):
    valide=True
    ## args[1] fichier zip sans l'extension 
    print(args[1])
    with zipfile.ZipFile(args[1]+".zip") as myzip:
        myzip.extractall()
        # student.json file 
    try:
        f=open(args[1]+"/student.json") 
        descriptor=json.load(f)
        print(descriptor["binomes"][0], descriptor["binomes"][1])
    except KeyError as e:
        valide=False
        print("no file student.json", file=sys.stderr)
    except json.decoder.JSONDecodeError as e:
        valide=False
        print(" file student.json not in JSON format",file=sys.stderr)
    # file liste 
    for name in filenamelist :
        try:
            print("testing "+args[1]+"/"+name)
            
            f=open(args[1]+"/"+name) 
        except KeyError as e:
            valide=False
            print("no file "+name, file=sys.stderr)
    # Does MOD.* exist
    MOD=False
    for name in ["/MOD.png","/MOD.jpg","/MOD.svg"]:
        if os.path.isfile(args[1]+name) :
            MOD=True
            print("MOD existe",name)
            break
    if not MOD:
        valide=False
        print(" Fichier MOD manquant",file=sys.stderr)
    # verification des fichier csv  loadcsv
    if not verifcsv(open(args[1]+"/"+"acteur.csv","r"),HEADERS['acteur']):
        print("Header invalides dans le fichier acteurs.csv",file=sys.stderr)
    else:
        print("acteurs ok")


    try:

        if not  verifcsv(open(args[1]+"/"+"concept.csv"),HEADERS['concept']):
            print("Header invalides dans le fichier concepts.csv",file=sys.stderr)
        if not verifcsv(open(args[1]+"/"+"usecase.csv"),HEADERS['usecase']):
            print("Header invalides dans le fichier usecase.csv",file=sys.stderr)
        if not   verifcsv(open(args[1]+"/"+"objectif.csv"),HEADERS['objectif']):
            print("Header invalides dans le fichier objectif.csv",file=sys.stderr)
    except Exception as e:
        print(e)
        print(" Problème de verification d'un CSV ",file=sys.stderr)
        print(" can't manage the problem balling out", file=sys.stderr)
        sys.exit(1)
    # chargement 
    try:
        l=[]
        for name in ["acteur.csv","objectif.csv","concept.csv","usecase.csv"]:
            print(name)
            l.append(loadcsv(open(args[1]+"/"+name)))
            print(name)

    except Exception as e:
        print(" Problème de lecture d'un CSV ",file=sys.stderr)
        print(" can't manage the problem balling out", file=sys.stderr)
        sys.exit(1)

    if valide:
        print("OK valide pour l'evaluation c'est plus tard. Vous pouvez uploader.")
    else:
        print("Réalisez les corrections nécessaires avant d'uploader sur moodle. Merci.")


    #import evaluation 
    #evaluation.coherence(*l,descriptor)

    return 0

if __name__ == '__main__':
    import sys
    print(sys.argv[1])
    if sys.argv[1]=="-h":
        print(" python3 verifcsv.py zipfilename # withou the .zip")
    if sys.argv[1]=="-b":
        # build a empty repertory with the good files 
        build(sys.argv[2])
        sys.exit(0)
    sys.exit(main(sys.argv))
