from plantes import Plante, plantes
from mesures import mesures


#Question 1
def croissance_moyenne(plantes):
    """
    Renvoie la moyenne des durées de croissance d'une liste (en jours), ou renvoie None si la liste est vide
    :param plantes: (list) Une liste de plantes de la classe Plante
    :return: (float or None) La moyenne des durées de croissance des plantes, ou None
    """
    assert isinstance(plantes, list),"plantes doit être une liste"
    for plante in plantes:
        assert isinstance(plante, Plante),"La liste doit contenir des plantes de la classe Plante"
    
    res = None
    somme = 0
    
    if len(plantes)!=0:
        for plante in plantes:
            somme+=plante.croissance
        res = somme/len(plantes)
        
    return res
       
       

assert croissance_moyenne(plantes)==79.0,"Erreur 1"
assert croissance_moyenne([]) is None,"Erreur 2"


#Question 2
def dictionnaire_mesure(plantes, mesures):
    """
    Renvoie un dictionnaire où chaque clé est le nom d'une plante de la liste plantes, associée une liste de mesures concernant cette plante
    :param plantes: (list) Une liste de plantes issus de la classe Plante
    :param mesures: (list) Une liste de dictionnaires représentant des mesures
    :return: (dict) Un dictionnaire
    """
    assert isinstance(plantes, list),"plantes doit être une liste"
    for plante in plantes:
        assert isinstance(plante, Plante),"La liste plantes doit contenir des plantes de la classe Plante"
    assert isinstance(mesures, list),"mesures doit être une liste"
    for mesure in mesures:
        assert isinstance(mesure, dict),"La liste mesures doit contenir des mesures sous la forme de dictionnaires"
    
    res = {}
    for plante in plantes:
        res[plante.nom] = []
        
    for mesure in mesures:
        if mesure["plante"] in res:
            res[mesure["plante"]].append(mesure)
            
    return res
    
    
assert dictionnaire_mesure(plantes[:2], mesures[:8])=={'Basilic': [{'jour': 1, 'plante': 'Basilic', 'hauteur': 0.85, 'temperature': 29.3, 'humidite': 50.89}, {'jour': 2, 'plante': 'Basilic', 'hauteur': 1.7, 'temperature': 17.44, 'humidite': 78.99}], 'Tomate': [{'jour': 1, 'plante': 'Tomate', 'hauteur': 1.27, 'temperature': 21.51, 'humidite': 47.19}, {'jour': 2, 'plante': 'Tomate', 'hauteur': 2.4, 'temperature': 18.98, 'humidite': 41.78}]},"Erreur 1"
assert dictionnaire_mesure(plantes, [])=={'Basilic': [], 'Tomate': [], 'Menthe': [], 'Tournesol': [], 'Fougère': []},"Erreur 2"



#Question 3
def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            liste_mesures.remove(mesure)


# def test_purger():
#     mesures_test = [
#         {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
#         {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
#         {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
#         {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
#         {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
#     ]
# 
#     purger_mesures_extremes(mesures_test)
# 
#     print("Résultat après la purge :")
#     for m in mesures_test:
#         print(f"Jour {m['jour']} : {m['temperature']}°C")
# 
# test_purger()



# Question 4
def purger_corrige(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    res = []
    for mesure in liste_mesures:
        if mesure['temperature'] > 20 and mesure['temperature'] < 25:
            res.append(mesure)
    return res
            

def test_purger_corrige():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]

    mesures_purgees = purger_corrige(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_purgees:
        print(f"Jour {m['jour']} : {m['temperature']}°C")
        

# test_purger_corrige()