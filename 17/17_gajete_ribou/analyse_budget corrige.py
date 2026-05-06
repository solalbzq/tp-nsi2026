import csv

def lire_mouvements_depuis_csv(nom_fichier_csv):
    """
    Lit les données d'un fichier CSV et les retourne en liste de dictionnaires.
    Les colonnes 'montant' et 'mois' sont converties respectivement en flottant et en entier.
    """
    mouvements_csv = []
    try:
        with open(nom_fichier_csv, mode='r', newline='', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                ligne['montant'] = float(ligne['montant'])
                ligne['mois'] = int(ligne['mois'])
                mouvements_csv.append(ligne)
        return mouvements_csv
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier_csv}' est introuvable.")
        return []

mouvements_test = [
    {'type': 'recette', 'catégorie': 'cotisations', 'montant': 1200.0, 'mois': 1},
    {'type': 'recette', 'catégorie': 'billetterie', 'montant': 300.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'fonctionnement', 'montant': 450.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'déplacements', 'montant': 200.0, 'mois': 12},
    {'type': 'dépense', 'catégorie': 'salaires', 'montant': 1500.0, 'mois': 12},
    {'type': 'recette', 'catégorie': 'subventions', 'montant': 800.0, 'mois': 12}
]

#############################################################################
# Écrire ci-dessous la fonction total_par_type et ses tests (Question 1)    #
#############################################################################

def total_par_type(mouvements,type_mouvement):
    """
    Renvoie la somme totale des montants selon le type de mouvement.
    :param mouvements:(list) la liste qui contient les mouvements.
    :param type_mouvements:(str) le type de mouvement dont on veut la somme totale.
    :return:(int) la somme totale.
    flemme de faire maintenant
    """
    assert type(mouvements)==list,"mouvements doit etre une liste"
    for i in range(len(mouvements)):
        assert type(mouvements[i])==dict,"tous les elements de mouvements doivent etre des dictionnaires"
        assert "type" in mouvements[i],"le type de mouvement doit etre inclu dans les dictionnaires dans mouvements."
        assert "montant" in mouvements[i],"le montant des mouvements doit etre inclu dans les dictionnaires dans mouvements."
        assert mouvements[i]["type"]=="recette" or mouvements[i]["type"]=="dépense","le type de mouvement dans les dictionnaires dans mouvements doit etre soit de la recette ou de la depense."
        assert type(mouvements[i]["montant"])==float or type(mouvements[i]["montant"]==int),"les montants dans les dictionnaires dans mouvements doivent etre des entiers ou des flottants."
    assert type_mouvement=="dépense" or type_mouvement=="recette","le type de mouvement doit etre une depense ou une recette"
    
    total = 0
    
    for i in range(len(mouvements)):
            if mouvements[i]["type"] == type_mouvement:
                total += mouvements[i]["montant"]
    return total


def test_total():
    assert total_par_type(mouvements_test,"recette")==2300
    assert total_par_type(mouvements_test,"dépense")==2150
    
#############################################################################
# Fonctions de calcul du solde (Questions 2 et 3)                           #
#############################################################################

def solde_mensuel(mouvements, mois):
    """
    Calcule le solde pour un mois donné (recettes - dépenses).
    """
    total_recettes = 0
    total_depenses = 0

    for m in mouvements:
        if m['mois'] == mois:
            if m['type'] == 'recette':
                total_recettes += m['montant']
            else:
                total_depenses += m['montant']

    return total_recettes - total_depenses


def solde_annuel(mouvements):
    """
    Calcule le solde annuel en additionnant les soldes de chaque mois.
    """
    total = 0
    # Parcourt les mois de l'année pour cumuler le bilan
    for m in range(1,13):
        total = total + solde_mensuel(mouvements, m)

    return total


    
#############################################################################
# Écrire ci-dessous la fonction test_solde_annuel (Question 2)              #
#############################################################################

def test_solde_annuel():
    assert solde_annuel(mouvements_test)==150

#############################################################################
# Programme principal pour analyser le fichier complet                      #
#############################################################################

mouvements_complets = lire_mouvements_depuis_csv("budget_complet.csv")
print("Le solde annuel sur le fichier complet est de :", solde_annuel(mouvements_complets))