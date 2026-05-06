def croissance_moyenne():# à complété



def dictionnaire_mesure():# à complété


def purger_mesures_extremes(mesures):
    for mesure in mesures:
        if mesure["temperature"] < 20 or mesure["temperature"] > 25:
            mesures.remove(mesure)  
    return mesures

