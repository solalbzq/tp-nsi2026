# ///////////////////////////////////////////////////////////////////////////
# FONCTIONS DONNEES
# ///////////////////////////////////////////////////////////////////////////

def recupere_donnees_fichier_csv(nom_fichier):
    """ Fonction qui récupère les données relevées du ballon sonde sans les en-têtes de la 1ère ligne """
    altitudes = []                                  # Initialisation des listes de valeurs relevées
    temperatures = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier csv au format npm.csv en mode "read"
    contenu_fichier = open(nom_fichier, 'r')
    # Supprime la 1ère ligne avec les en-têtes
    contenu_fichier.readline()
    # Parcours des lignes du fichier csv contenant les donnees relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les \n et espaces en fin de ligne
        ligne = ligne.rstrip()
        # création d'une listeValeurs. split(";") sépare les valeurs grâce au ;
        listeValeurs = ligne.split(";")
        # conversion string en int de l'altitude et insertion dans la liste correspondante
        altitudes.append(int(listeValeurs[0]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        temperatures.append(float(listeValeurs[1]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        longitudes.append(float(listeValeurs[2]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        latitudes.append(float(listeValeurs[3]))
    return altitudes, temperatures, longitudes, latitudes


def genere_kml(liste_longitudes, liste_latitudes):
    """ Fonction qui génère un fichier de données géographiques au format standard international KML
        Ce fichier est visionnable ensuite dans différents logiciels
    """
    assert len(liste_longitudes) == len(liste_latitudes), "Les listes de longitudes et de latitudes doivent avoir la même taille"
    fichier_kml = open(
        'ballon sonde.kml', 'w')    # Création et ouverture du fichier kml en mode "write"
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    entete_fichier += '<Document>\n'
    entete_fichier += '<name>Trajectoire ballon sonde</name>\n'
    # Ecriture du contenu de la variable entete_fichier dans le fichier kml
    fichier_kml.write(entete_fichier)
    for i in range(len(liste_longitudes)):
        corps_fichier = '<Placemark>\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '<Point>\n'
        corps_fichier += f'<coordinates>{liste_longitudes[i]},{liste_latitudes[i]}</coordinates>\n'
        corps_fichier += '</Point>\n'
        corps_fichier += '</Placemark>\n'
        fichier_kml.write(corps_fichier)
    bas_fichier = '</Document>\n</kml>\n'
    fichier_kml.write(bas_fichier)
    fichier_kml.close()                         # Fermeture du fichier kml


# ///////////////////////////////////////////////////////////////////////////
# TRAVAIL DEMANDE
# ///////////////////////////////////////////////////////////////////////////

# QUESTION 1
altitudes, temperatures,longitudes, latitudes = recupere_donnees_fichier_csv("releves_ballon_sonde.csv")

# QUESTION 2
def conversion_K_en_C(liste_temperatures):
    """
    convertit une liste de températures en kelvins en degrés celsius
    :param liste_temp:(list) liste représentant des températures en kelvins
    :return:(list) liste représentant des températures en celsius
    :Exemple:
    >>> conversion_K_en_C(temperatures)
    [15.0, 13.7, 11.7, 7.9, 3.4, 0.5, -2.3, -17.7, -28.9, -42.5, -48.3, -56.0,
    -56.2, -56.5, -56.5, -56.0, -56.1, -53.0, -50.1, -48.0]
    >>> conversion_K_en_C([273.15])
    [0]
    >>> conversion_K_en_C(3)
    Traceback(most recent call last):
    ...
    AssertionError: liste_temperatures doit être une liste
    >>> conversion_K_en_C([temp])
    Traceback(most recent call last):
    ...
    AssertionError: les éléments de liste_temperatures doivent être des entiers ou des flottants
    >>> conversion_K_en_C([])
    Traceback(most recent call last):
    ...
    AssertionError: liste_temperatures doit être une liste non vide 
    """
    assert isinstance(liste_temperatures, list),"liste_temperatures doit être une liste"
    assert len(liste_temperatures)!= 0, "liste_temperatures doit être une liste non vide"
    for elem in liste_temperatures:
        assert isinstance(elem, int) or isinstance(elem, float), " les éléments de liste_temperatures doivent être des entiers ou des flottants"
    liste_celsius = []
    for k in liste_temperatures:
        temp_c = round(k-273.15, 1)
        liste_celsius.append(temp_c)
    return liste_celsius

# QUESTION 3
def altitude_la_plus_froide(liste_altitudes, liste_temperatures):
    """
    renvoie la température la plus froide, ainsi qu’une liste contenant les altitudes correspondantes.
    :param liste_temp:(list) liste représentant des températures en kelvins
    :return:(list) liste représentant des températures en celsius
    :Exemple:
    >>> altitude_la_plus_froide(altitudes,temperatures)
    (216.65, [15120, 17210])
    >>> altitude_la_plus_froide([15120], [216.65])
    (216.65, [15120])
    >>> altitude_la_plus_froide(3,temperatures)
    Traceback(most recent call last):
    ...
    AssertionError: liste_altitudes doit être une liste
    >>> altitude_la_plus_froide(altitudes,3)
    Traceback(most recent call last):
    ...
    AssertionError: liste_temperatures doit être une liste
    >>> altitude_la_plus_froide([],temperatures)
    Traceback(most recent call last):
    ...
    AssertionError: liste_altitudes doit être une liste non vide
    >>> altitude_la_plus_froide(altitudes,[])
    Traceback(most recent call last):
    ...
    AssertionError: liste_temperatures doit être une liste non vide
    >>> altitude_la_plus_froide([altitude],temperatures)
    Traceback(most recent call last):
    ...
    AssertionError: les éléments de liste_altitudes doivent être des entiers
    >>> altitude_la_plus_froide(altitudes,[temperature])
    Traceback(most recent call last):
    ...
    AssertionError: les éléments de liste_temperatures doivent être des entiers ou des flottants
    """
    assert isinstance(liste_altitudes, list),"liste_altitudes doit être une liste"
    assert len(liste_altitudes)!= 0, "liste_altitudes doit être une liste non vide"
    for elem in liste_altitudes:
        assert isinstance(elem, int),"les éléments de liste_altitudes doivent être des entiers"
    assert isinstance(liste_temperatures, list),"liste_temperatures doit être une liste"
    assert len(liste_temperatures)!= 0, "liste_temperatures doit être une liste non vide"
    for elem in liste_temperatures:
        assert isinstance(elem, int) or isinstance(elem, float), "les éléments de liste_temperatures doivent être des entiers ou des flottants"
    temp_min = liste_temperatures[0]
    for temp in liste_temperatures:
        if temp < temp_min:
            temp_min = temp
    altitudes_min = []
    for i in range(len(liste_altitudes)):
        if liste_temperatures[i] == temp_min:
            altitudes_min.append(liste_altitudes[i])
    return (temp_min, altitudes_min)

# AUTRES ELEMENTS DE CODE
# QUESTION 5
genere_kml(longitudes, latitudes)