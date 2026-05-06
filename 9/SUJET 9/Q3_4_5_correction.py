from Q2_correction import Objet3D

#############################################################################
# Variables et fonctions fournies pour la question 3                        #
#############################################################################
parametres_imprimante = {'remplissage': 20,
                         'vitesse_extrusion': 8}  # 8mm3 / seconde

def volume_cube(cube): #INUTILE DANS L'ANCIEN SUJET 
    a, b = cube.sommets_adjacents()
    taille_cote = a.distance(b)  # distance donnee en mm
    return taille_cote ** 3

#############################################################################
# Écrire le code de la fonction estimation_impression de la question 3      #
#############################################################################
def estimation_impression(volume_reel,d):
    """
    renvoie le total d'impression sous la forme d'un float les secondes nécéssaires à l'impression
    :param volume: (int) volume de l'objet à imprimer
    :param d: (dict) contenant les informations de l'imprimante
    :return: (float) renvoie le total d'impression
    """
    assert isinstance(volume_reel,int), "volume doit être un entier"
    assert isinstance(d,dict) and d.get("remplissage") and d.get("vitesse_extrusion") and d["vitesse_extrusion"] > 0, "dictionnaire remplit nécéssaire"
     
    vol_impression = volume_reel * d['remplissage'] / 100
    return vol_impression / d['vitesse_extrusion']

#############################################################################
# Programme à modifier de la question 4 et 5                                #
#############################################################################

if __name__ == "__main__":
    #QUESTION 3
    estimation_impression(10000, parametres_imprimante)

    #QUESTION 4
    objet = Objet3D()
    objet.ajouter_sommet(0, 0, 0) #1
    objet.ajouter_sommet(0, 2, 0) #2
    objet.ajouter_sommet(2, 2, 0) #3
    objet.ajouter_sommet(2, 0, 0) #4
    objet.ajouter_sommet(1, 1, 2) #5
    
    objet.ajouter_face([1, 2, 3, 4])
    objet.ajouter_face([1, 2, 5])  
    objet.ajouter_face([2, 3, 5])  
    objet.ajouter_face([3, 4, 5])  
    objet.ajouter_face([4, 1, 5]) 

    objet.afficher()

    #QUESTION 5
    copie = objet.transformer(2)
    copie.afficher()
