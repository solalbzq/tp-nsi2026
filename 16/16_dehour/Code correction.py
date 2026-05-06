import csv
import matplotlib.pyplot as plt

def charger(nom_fichier):
    """
    Lit un fichier CSV (contenant les colonnes 'Year' et 'Anomaly') 
    et renvoie une liste de dictionnaires correctement typés.
    """
    donnees = []
    with open(nom_fichier, mode='r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            annee = int(ligne["Year"])
            ecart = float(ligne["Anomaly"])
            donnees.append({"année": annee, "écart": ecart})
    return donnees

datas_temperature = charger("datas.csv")



#Question 1
def ecart_temperature(datas, annee):
    """
    Renvoie l'écart de température d'une année passée en paramètre lorsqu'elle est dans une liste de dictionnaires datas, ou renvoie None si l'année n'est pas dans datas
    :param datas: (list) Une liste de dictionnaires
    :param annee: (int) L'année dont on veut connaitre l'écart
    :cu: L'année doit être strictement positive
    :return: (int or float or None) L'écart ou None
    """
    assert isinstance(datas, list),"Datas doit être une liste de dictionnaires"
    assert isinstance(annee, int),"L'année cible doit être un entier"
    for element in datas:
        assert isinstance(element, dict),"La liste datas ne doit contenir que des dictionnaires"
        assert isinstance(element["année"], int),"Les dictionnaires de datas doivent avoir une clé année valide"
        assert element["année"]>=0,"La clé année des dictionnaires doit être positive ou nulle"
    assert annee>=0,"L'année cible doit être positive ou nulle"
    
    res=None
    for dictionnaire in datas:
        if dictionnaire["année"] == annee:
            res = dictionnaire["écart"]
    return res
    
    
assert ecart_temperature(datas_temperature, 1920)==-0.24,"Erreur 1"
assert ecart_temperature(datas_temperature, 2039) is None,"Erreur 2"




def derniere_annee_ecart_negatif(datas):
    annee = max([element["année"] for element in datas])
    ecart = ecart_temperature(datas, annee)
    while ecart >= 0:
        annee = annee - 1
        ecart = ecart_temperature(datas, annee)
    return annee



#Question 2
derniere_annee = derniere_annee_ecart_negatif(datas_temperature)
print(f"La dernière année avec un écart négatif est {derniere_annee}")




def moyenne_ecarts(annee_debut, annee_fin, datas):
    """
    Renvoie la moyenne des écarts de température pour la période comprise 
    entre annee_debut et annee_fin (incluses).
    """
    somme = 0
    compteur = 0
    for dico in datas:
        if annee_debut <= dico["année"] and dico["année"] <= annee_fin:
            somme = somme - dico["écart"]
            compteur += 1
    return somme / compteur



#Question 3
def moyenne_ecarts_corrige(annee_debut, annee_fin, datas):
    """
    Renvoie la moyenne des écarts de température pour la période comprise 
    entre annee_debut et annee_fin (incluses).
    """
    somme = 0
    compteur = 0
    for dico in datas:
        if annee_debut <= dico["année"] and dico["année"] <= annee_fin:
            somme = somme + dico["écart"]
            compteur += 1
    return somme / compteur



def prevision(datas, annee, n):
    """
    Renvoie l'écart de température attendu calculé par régression linéaire 
    sur les n dernières années.
    """
    longueur = len(datas)
    annee_debut = datas[longueur-n]["année"]
    annee_fin = datas[longueur-1]["année"]

    moy_annees = (annee_debut + annee_fin) / 2
    moy_temperatures = moyenne_ecarts_corrige(annee_debut, annee_fin, datas)

    numerateur = 0
    denominateur = 0
    for i in range(1, n+1):
        ecart_annee = datas[longueur-i]["année"] - moy_annees
        ecart_temp = datas[longueur-i]["écart"] - moy_temperatures
        numerateur += ecart_annee * ecart_temp
        denominateur += ecart_annee ** 2

    a = numerateur / denominateur
    b = moy_temperatures - a * moy_annees

    return a * annee + b



def graphique(datas):
    """
    Représente visuellement les warming stripes.
    """
    fig, ax = plt.subplots(figsize=(10, 2))

    # Création d'une palette de couleurs basée sur l'amplitude thermique
    cmap = plt.get_cmap("seismic")
    temperatures = [dico["écart"] for dico in datas]
    max_val = max(max(temperatures), -min(temperatures))
    norm = plt.Normalize(-max_val, max_val)

    #Question 4
    annees = []
    ordonnees = []
    for dictionnaire in datas:
        annees.append(dictionnaire['année'])
        ordonnees.append(1)
        
    # Génération du graphique
    ax.bar(annees, ordonnees, width=1.0, color=cmap(norm(temperatures)))
    ax.set_title("Warming Stripes mondiales - Base 1901-2000")
    plt.yticks([], [])  # Masque l'axe Y car seule la couleur compte
    ax.set_xlabel("Année")

    plt.tight_layout()
    plt.show()