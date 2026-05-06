# =================================================================================#
# Données de test
donnees_test = [
    # Société - Données sur 2010 et 2020
    {'date': '2010-01-15', 'zone': 'Societe', 'temperature': 27.0},
    {'date': '2010-06-20', 'zone': 'Societe', 'temperature': 26.5},
    {'date': '2011-03-10', 'zone': 'Societe', 'temperature': 27.5},
    {'date': '2020-02-14', 'zone': 'Societe', 'temperature': 28.0},
    {'date': '2020-08-22', 'zone': 'Societe', 'temperature': 28.5},
    {'date': '2021-05-30', 'zone': 'Societe', 'temperature': 29.0},

    # Tuamotu - Données sur 2010 et 2020
    {'date': '2015-04-10', 'zone': 'Tuamotu', 'temperature': 26.8},
    {'date': '2020-07-15', 'zone': 'Tuamotu', 'temperature': 27.5},
    {'date': '2021-09-20', 'zone': 'Tuamotu', 'temperature': 28.0},

    # Marquises - Données uniquement sur 2020
    {'date': '2020-03-15', 'zone': 'Marquises', 'temperature': 25.5},
    {'date': '2021-07-10', 'zone': 'Marquises', 'temperature': 26.0},
    {'date': '2022-11-25', 'zone': 'Marquises', 'temperature': 26.5},
]

# =================================================================================#
#  Question 1 : Ecrire le code de votre fonction température_moyenne

def temperature_moyenne(zone, donnees):
    somme=0
    nb_temp=0
    for i in donnees:
        if i['zone']==zone:
            somme+=i['temperature']
            nb_temp+=1
    if nb_temp==0:
        res=None
    else:
        res=somme/nb_temp
    return res
            
# =================================================================================#
#  Question 2 : Ecrire le code de votre fonction detection_anomalies

def detecter_anomalies(zone, seuil, donnees):
    temp_moy=temperature_moyenne(zone, donnees)
    anomalies=[]
    if temp_moy==None:
        return []
    else:
        for i in donnees:
            if i['zone']==zone and abs(i['temperature']-temp_moy)>seuil:
                anomalies.append(i['date'])
        return anomalies
    
# =================================================================================#
# code de la fonction evolution_par_decennie à corriger dans la question 4:


def evolution_par_decennie(zone, donnees):
    """
    Calcule l'évolution des températures moyennes par décennie pour une zone.

    ATTENTION: Cette fonction contient un bug volontaire à détecter et corriger.

    Arguments:
        zone (str): Nom de l'archipel (ex: 'Societe', 'Tuamotu')
        donnees (list): Liste de dictionnaires de relevés

    Renvoie:
        dict: Dictionnaire {décennie : température_moyenne}
              ex: {2010: 27.5, 2020: 28.3}
              Renvoie un dictionnaire vide si la zone n'existe pas
    """
    # Filtrage des relevés pour la zone
    releves_zone = [r for r in donnees if r['zone'] == zone]

    if not releves_zone:
        return {}

    # Regroupement par décennie
    temperatures_par_decennie = {}

    for releve in releves_zone:
        # Extraction de l'année de la date (format: 'YYYY-MM-DD')
        annee = int(releve['date'].split('-')[0])

        # Calcul de la décennie
        decennie = (annee // 10)*10

        if decennie not in temperatures_par_decennie:
            temperatures_par_decennie[decennie] = []

        temperatures_par_decennie[decennie].append(releve['temperature'])

    # Calcul des moyennes
    moyennes = {}
    for decennie, temperatures in temperatures_par_decennie.items():
        moyennes[decennie] = round(sum(temperatures) / len(temperatures), 2)

    return moyennes


# =================================================================================#
#  Exercice 2.1 :
"""
Tests
À compléter par le candidat dans le cadre de la question 3
"""


def test_zone_inexistante():
    """
    Test 1 : Tester une zone qui n'existe pas

    À compléter:
    1. Appeler evolution_par_decennie avec une zone inexistante
    2. Vérifier que le résultat est un dictionnaire vide
    """
    resultat=evolution_par_decennie('Zone_inexistante', donnees_test)
    assert resultat=={}

def test_une_seule_decennie():
    """
    Test 2: Tester une zone avec données sur une seule décennie

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat ne contient qu'une seule décennie (2020)
    3. Vérifier la température moyenne
    """
    resultat=evolution_par_decennie('Marquises', donnees_test)
    assert len(resultat)==1
    assert 2020 in resultat
    assert resultat[2020]==26.0


def test_plusieurs_decennies():
    """
    Test 3 : Tester une zone avec données sur plusieurs décennies

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat contient bien les clés 2010 et 2020
    3. Vérifier que les températures moyennes sont cohérentes
    """
    resultat=evolution_par_decennie('Societe', donnees_test)
    assert len(resultat)>=2
    assert resultat[2010]==27.0
    assert resultat[2020]==28.5