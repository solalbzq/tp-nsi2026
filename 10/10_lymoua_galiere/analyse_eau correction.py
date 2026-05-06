donnees = [
    {"jour": "2025-02-04", "heure": "00:00", "chaude": 2, "froide": 3},
    {"jour": "2025-02-04", "heure": "01:00", "chaude": 1, "froide": 2},
    {"jour": "2025-02-04", "heure": "02:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "03:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "04:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-04", "heure": "05:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "06:00", "chaude": 4, "froide": 6},
    {"jour": "2025-02-04", "heure": "07:00", "chaude": 6, "froide": 8},
    {"jour": "2025-02-05", "heure": "00:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "01:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "02:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "03:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "04:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "05:00", "chaude": 0, "froide": 0},
]


# -----------------------------
# Fonctions à compléter
# -----------------------------

def total_conso(donnees, jour):
    total = 0
    resultat = False
    for mesure in donnees:
        if mesure["jour"] == jour:
            total += mesure["chaude"] + mesure["froide"]
            resultat = True
    if resultat:
        return total
    return None

def fuite_possible(donnees, jour):
    compteur = 0
    for mesure in donnees:
        if mesure["jour"] == jour:
            heure = mesure["heure"]
            if "00:00" <= heure <= "05:00":
                conso = mesure["chaude"] + mesure["froide"]
                if conso > 0:
                    compteur += 1
                    if compteur >= 3:
                        return True
                else:
                    compteur = 0
    return False


# -----------------------------
# Fonction fournie (erronée)
# -----------------------------

def lissage_conso(valeurs):
    """
    Calcule une moyenne glissante sur les valeurs.
    Pour chaque valeur, on calcule la moyenne avec ses voisins.
    """   
    lisse = []
    for i in range(len(valeurs)):
        if i == 0:
            m = (valeurs[i] + valeurs[i+1]) / 2
        elif i == len(valeurs)-1:
            m = (valeurs[i-1] + valeurs[i]) / 2
        else:
            m = (valeurs[i-1] + valeurs[i] + valeurs[i+1]) / 3
        lisse.append(m)
    return lisse


# -----------------------------
# Espace pour les tests
# -----------------------------

def test_lissage():
    assert lissage_conso([10])==[10]
    assert lissage_conso([10, 20, 33, 40, 50])==[15.0, 21.0, 31.0, 41.0, 45.0]
    assert lissage_conso([10, 2])==[6.0, 6.0]