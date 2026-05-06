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

def total_conso(donnees, jour):
    total = 0
    bol = False
    
    for mesure in donnees:
        if mesure["jour"] == jour:
            total = total + mesure["chaude"] + mesure["froide"]
            bol = True
    
    if bol:
        return total
    else:
        return None


def fuite_possible(donnees, jour):
    heures_nuit = {"00:00", "01:00", "02:00", "03:00", "04:00", "05:00"}

    mesures_nuit = [
        m for m in donnees
        if m["jour"] == jour and m["heure"] in heures_nuit
        ]

    compteur_consecutif = 0
    for mesure in mesures_nuit:
        conso = mesure["chaude"] + mesure["froide"]
        if conso > 0:
            compteur_consecutif += 1
            if compteur_consecutif >= 3:
                return True
        else:
            compteur_consecutif = 0  

    return False

def lissage_conso(valeurs):
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


test = [10, 20, 30, 40, 50]
lissage_conso(test)


# fonction corrigée
def lissage_conso(valeurs):
    if len(valeurs) == 1:
        return valeurs
    
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

# Appel des test, plus d'erreur :)
test_lissage()