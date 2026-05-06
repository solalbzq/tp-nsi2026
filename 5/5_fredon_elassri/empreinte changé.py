import os
import os.path
import json

########### Fonctions données ###########

def chargement_json(nom_fichier):
    """Charge le contenu d'un fichier JSON dans un dictionnaire Python renvoyé"""
    with open(nom_fichier, "r", encoding="utf8") as curseur:
        return json.load(curseur)


def sauvegarde_json(dictionnaire, nom_fichier):
    """Sauvegarde le contenu d'un dictionnaire dans un fichier JSON"""
    with open(nom_fichier, "w", encoding="utf8") as curseur:
        json.dump(dictionnaire, curseur)


def est_dictionnaire(objet):
    """Teste si un objet est de type dictionnaire"""
    return isinstance(objet, dict)


##########################################

def total_simple(empreinte):
    """Fonction qui renvoie l'empreinte carbone totale d'un dictionnaire associant
    une empreinte carbone à des noms de catégories"""
    total = 0
    for cle, valeur in empreinte.items():
        total += valeur
    return total

def test_total_simple():
    # On récupère le dictionnaire à partir du JSON
    empreinte = chargement_json("empreinte_ada_agr.json")
    assert total_simple(empreinte) == 7252


def total_rec(empreinte):
    """Fonction récursive qui renvoie l'empreinte carbone totale représentée
    par un dictionnaire dont les valeurs peuvent aussi être des dictionnaires"""
    total = 0
    if est_dictionnaire(empreinte):
        for cle, valeur in empreinte.items():
            total = total + total_rec(valeur)
        return total
    else:
        return empreinte
    
def test_total_rec():
    test_dico1 = {"a": 1, "d": 2}
    assert total_rec(test_dico1) == 3
    test_dico2 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert total_rec(test_dico2) == 6
    # On récupère le dictionnaire à partir du JSON
    empreinte = chargement_json("empreinte_ada.json")
    assert total_rec(empreinte) == 7252

def alerte_valeur_aberrante_aux(empreinte, limite):
    """
    Fonction qui compte récursivement les
    valeurs aberrantes
    """
    nb = 0
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            nb += alerte_valeur_aberrante(valeur, limite)
        else:
            if valeur > limite:
                nb += 1
    return nb

def alerte_valeur_aberrante(empreinte, limite):
    """
    Fonction qui détermine si au moins une valeur du dictionnaire
    dépasse strictement la limite donnée.
    """
    if alerte_valeur_aberrante_aux(empreinte, limite) > 0:
        return True
    else:
        return False