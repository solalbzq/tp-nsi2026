import calendar

#############################################################################
# Écrire le code de la fonction est_bissextile de la question 1             #
#############################################################################

def est_bissextile(annee):
    """
    Prend en parametre une annee et renvoie si elle est ou non bissextile
    :param annee:(int) l'annee dont on verifie la "bissextilite"
    """
    assert type(annee)==int,"l'annee doit etre un nombre entier"
    res = False 
    if annee%4==0 and (annee%400==0 or annee%100!=0):
        res = True
    return res
    
#############################################################################
# Écrire le code de la fonction determiner_phase de la question 2           #
#############################################################################

def determiner_phase(jour):
    """
    Prend en parametre un entier jour qui correspond a un jour du cycle,
    et renvoie un entier correspondant a la phase du cycle associee a ce jour
    :param jour:(int) le jour du cycle dont on veut obtenir la phase associee
    :cu: jour doit etre entre 1 et 28 inclus
    """
    assert type(jour)==int,"jour doit etre un entier"
    assert jour >= 1 and jour <= 28,"jour doit etre entre 1 et 28 inclus"
    
    res = None 
    if jour >= 1 and jour <= 5:
        res = 1
    elif jour >= 6 and jour <= 13:
        res = 2
    elif jour==14:
        res = 3
    else:
        res = 4
    return res
    
#############################################################################
# Fonctions fournies pour la question 3                                     #
#############################################################################
def jours_dans_mois(annee, mois):
    """Renvoie le nombre de jours dans un mois donné d'une année donnée.
       Utilise le module calendar pour gérer les années bissextiles."""
    if mois == 2:  # février
        return 29 if calendar.isleap(annee) else 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def ajouter_jours(date, nb_jours):
    """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
       La date est représentée par un tuple (jour, mois, année)."""
    jour, mois, annee = date
    jour = jour + nb_jours

    # Ajustement du jour et du mois si dépassement
    while jour > jours_dans_mois(annee, mois):
        jour = jour - jours_dans_mois(annee, mois)
        mois = mois + 1
        if mois > 12:  # passage à l'année suivante
            mois = 1
            annee = annee + 1

    return (jour, mois, annee)


def test_ajouter_jours():
    assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025) 
    assert ajouter_jours((28,1,2025),4) == (1,2,2025) #teste le changement de mois (sur un mois en 31)
    assert ajouter_jours((30,4,2025),1) == (1,5,2025) #teste le changement de mois (sur un mois en 30)
    assert ajouter_jours((28, 2, 2024),1) == (29, 2, 2024) #teste le changement de mois en annee bissextile
    assert ajouter_jours((28, 2, 2023),1) == (1, 3, 2023) #teste le changement de mois en annee non bissextile
    assert ajouter_jours((27,12,2025),5) == (1,1,2026) #teste le changement d'annee
    assert ajouter_jours((6,7,2025),30) == (5,8,2025) #teste laddition dun mois entier 
    assert ajouter_jours((6,7,2025),365) == (6,7,2026) #teste laddition dune annee entiere

#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################


def calendrier_cycles(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar, l'ensemble
    des dates de début de règles qui se présentent dans les 100 jours suivants 
    `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours. """

    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules + 28 <= 100:
        jour, mois, annee = date_courante
        cal_lignes.append('BEGIN:VEVENT')
        if jour > 9 and mois > 9:
            date = str(annee)+str(mois)+str(jour)
        elif jour > 9:
            date = str(annee)+str("0"+str(mois))+str(jour)
        elif mois > 9:
            date = str(annee)+str(mois)+str("0"+str(jour))
        else:
            date = str(annee)+str("0"+str(mois))+str("0"+str(jour))
        cal_lignes.append('DTSTART:'+date)
        cal_lignes.append('SUMMARY: Règles')
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28

    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)


def test_calendrier_cycles():
    '''Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité.

    Nécessite que le module ics soit présent sur la machine (pip install ics).
    '''
    from ics import Calendar
    c = calendrier_cycles((12, 3, 2026))
    print(c)
    cal = Calendar(c)
    print(cal.events)
