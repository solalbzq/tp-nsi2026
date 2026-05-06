# -----------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie

def est_en_penurie(liste,nom):
    for i in range (len(liste)):
        if liste[i]["nom"] == nom:
            if liste[i]["volume"]/liste[i]["capacite"]>0.23:
                return False
            else:
                return True

# Question 2 : écrire la fonction volume_par_district

def volume_par_district(liste):
    d={}
    for i in range(len(liste)):
        if liste[i]["district"] not in d:
            d[liste[i]["district"]]=liste[i]["volume"]
        else :
            d[liste[i]["district"]] = d[liste[i]["district"]] + liste[i]["volume"]
    return d 

# Question 3


def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    maxi=0
    for i in range(len(reservoirs)):
        if maxi == 0 :
            maxi = reservoirs[i]["volume"]
        elif maxi < reservoirs[i]["volume"]:
            maxi = reservoirs[i]["volume"] 
        else :
            pass
        
    assert len(reservoirs)>=1 , "au moins 1 reservoires "
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
        print(r["volume"])
    moyenne = somme_totale / (len(reservoirs)-1)
    print (somme_totale)
    assert moyenne <= maxi , "la moy doit etre inferieur ou egal a la valeur max des reservoirs sinon pas une moyenne "
    return moyenne

# Question 4


def eau_insufisante(liste):
    d={}
    moyenne=0
    mo=0
    for i in range(len(liste)):
        if liste[i]["district"] not in d:
            d[liste[i]["district"]]=liste[i]["volume"]
        else :
            d[liste[i]["district"]] = d[liste[i]["district"]] + liste[i]["volume"]
    for j in d.values():
        mo=j+mo
    moyenne = mo/len(d)
    print (moyenne)
    for q,v in d.items():
        if v < moyenne*0.80 :
            print (q ,"est en deficite")
        else :
            print(q,"est suffisant")


def liste_districts(reservoirs):
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd

#caca == élodie