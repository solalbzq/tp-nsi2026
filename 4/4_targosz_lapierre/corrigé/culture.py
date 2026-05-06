class Plante:
    def __init__(self, nom, espece, duree_croissance, taille_moyenne, exposition):
        self.nom = nom
        self.espece = espece
        self.duree_croissance = duree_croissance
        self.taille_moyenne = taille_moyenne      
        self.exposition = exposition  
plantes = [
    Plante("plante1", "tomate", 60, 150, "plein soleil"),
    Plante("plante2", "laitue", 45, 30, "mi-ombre"),
    Plante("plante3", "basilic", 30, 40, "plein soleil"),
    Plante("plante4", "menthe", 50, 60, "ombre"),
]
mesures = [
    # plante1 (tomate)
    {"plante": "plante1", "jour": 1, "hauteur": 12, "temperature": 22, "humidite": 65},
    {"plante": "plante1", "jour": 2, "hauteur": 18, "temperature": 24, "humidite": 70},
    {"plante": "plante1", "jour": 3, "hauteur": 25, "temperature": 26, "humidite": 75},  

    # plante2 (laitue)
    {"plante": "plante2", "jour": 1, "hauteur": 6, "temperature": 21, "humidite": 60},
    {"plante": "plante2", "jour": 2, "hauteur": 9, "temperature": 19, "humidite": 55},   
    {"plante": "plante2", "jour": 3, "hauteur": 12, "temperature": 23, "humidite": 58},

    # plante3 (basilic)
    {"plante": "plante3", "jour": 1, "hauteur": 8, "temperature": 20, "humidite": 65},
    {"plante": "plante3", "jour": 2, "hauteur": 13, "temperature": 22, "humidite": 68}

]


def croissance_moyenne(plantes):
    if len(plantes) == 0:
        return None
    
    total = 0
    for plante in plantes:
        total += plante.duree_croissance
    
    return total / len(plantes)


# Cas normal
p1=Plante("plante1", "tomate", 60, 150, "plein soleil")
p2=Plante("plante2", "laitue", 45, 30, "mi-ombre")
print(croissance_moyenne([p1, p2]))  # 52.5

# Cas liste vide
print(croissance_moyenne([]))  #  None



def dictionnaire_mesure(plantes, mesures):
    dico = {}


    for plante in plantes:
        dico[plante.nom] = []

    
    for mesure in mesures:
        nom_plante = mesure["plante"]
        if nom_plante in dico:
            dico[nom_plante].append(mesure)

    return dico



dico = dictionnaire_mesure(plantes, mesures)

#print(dico)







def purger_mesures_extremes(mesures):
    for mesure in mesures:
        if mesure["temperature"] < 20 or mesure["temperature"] > 25:
            mesures.remove(mesure)  # Erreur ici 
    return mesures
    
    
def corrigé_purger_mesures_extremes(mesures):
    resultat = []
    for mesure in mesures:
        if 20 <= mesure["temperature"] <= 25:
            resultat.append(mesure)
    return resultat
