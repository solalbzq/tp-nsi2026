from math import sqrt
from donnees_habitats import zones_connues

nouveau = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6 , 'presence_renard' : 0}


def distance(habitat_1, habitat_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    vegetation_1 = habitat_1['vegetation']
    proximite_eau_1 = habitat_1['proximite_eau']
    densite_urbaine_1 = habitat_1['densite_urbaine']
    disponibilite_proies_1 = habitat_1['disponibilite_proies']
    presence_renard_1 = habitat_1['presence_renard']
    
    vegetation_2 = habitat_2['vegetation']
    proximite_eau_2 = habitat_2['proximite_eau']
    densite_urbaine_2 = habitat_2['densite_urbaine']
    disponibilite_proies_2 = habitat_2['disponibilite_proies']
    presence_renard_2 = habitat_2['presence_renard']
    
    d = sqrt((vegetation_1 - vegetation_2)**2 + (proximite_eau_1 - proximite_eau_2)**2 + (densite_urbaine_1 - densite_urbaine_2)**2 + (disponibilite_proies_1 - disponibilite_proies_2)**2 + (presence_renard_1 - presence_renard_2)**2)
    return d

def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance entre habitat et chaque habitat de la liste.
    '''
    l= []
    for i in habitats:
        j = distance(habitat, i)
        l.append((j, i))

    return l

##################### QUESTION 3 ########################
res = distance_d_un_habitat(nouveau, zones_connues)
print(res[0])
print(res[1])
print(res[2])
#########################################################


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

##################### QUESTION 5 ########################
for k in range(1, 10):
    print(k, presence_renard(k, nouveau, zones_connues))
#Après avoir testé la fonction presence_renard pour plusieurs valeurs de k, on observe que dans la majorité des cas la fonction renvoie True. On en déduit donc que l’habitat étudié est susceptible de contenir une population de renards.
#########################################################
