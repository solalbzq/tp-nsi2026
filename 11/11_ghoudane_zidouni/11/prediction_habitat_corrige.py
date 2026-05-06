from math import sqrt
from donnees_habitats import zones_connues

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}

#Question 1 Fonction distance
def distance(habitat_1, habitat_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    return sqrt((habitat_1['vegetation'] - habitat_2['vegetation'])**2 + 
                (habitat_1['proximite_eau'] - habitat_2['proximite_eau'])**2 + 
                (habitat_1['densite_urbaine'] - habitat_2['densite_urbaine'])**2 + 
                (habitat_1['disponibilite_proies'] - habitat_2['disponibilite_proies'])**2)

#Question 2 : Fonction distance_d_un_habitat
def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance entre habitat et chaque habitat de la liste.
    '''
    res = []
    for h in habitats:
        dist = distance(habitat, h)
        res.append((dist, h))
    return res

#Question 3 : Test fonction distance_d_un_habitat
resultats = distance_d_un_habitat(nouveau, zones_connues[:3])
for dist, habitat in resultats[:3]:
    print(f"({dist}, {habitat})")

def k_plus_proches(k, habitat, habitats):
    '''
    Calcule les k habitats les plus proches de l'habitat donné.
    entrée : 
        - k : entier représentant le nombre d'habitats à retourner.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) l'élément à l'indice 0 est la distance euclidienne entre habitat 
                        et chaque habitat de la liste et l'élément à l'indice 1 est le dictionnaire correspondant à l'habitat correspondant.
    '''
    # On calcule les distances
    distances = distance_d_un_habitat(habitat, habitats)
    # On cherche à trier les distances en fonction de la distance euclidienne.
    distances.sort(key = lambda x: x[0])
    return distances[:k] # renvoie les distances jusque la borne k non comprise

#Question 4 : Correction de la fonction presence_renard
def presence_renard(k, habitat, habitats):
    '''
    Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    entrée : 
        - k : entier représentant le nombre d'habitats à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards, False sinon.
    '''
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats:
        distance = habitat[0]
        caracteristiques = habitat[1]
        if caracteristiques['presence_renard'] == 1:
            n_renards += 1
    return n_renards > k/2

#Question 5 : Test fonction presence_renard
for k in (1, 3, 5, 7, 9, 11):
    if presence_renard(k, nouveau, zones_connues):
        print(f"k = {k}: Susceptible")
    else:
        print(f"k = {k}: Non susceptible")