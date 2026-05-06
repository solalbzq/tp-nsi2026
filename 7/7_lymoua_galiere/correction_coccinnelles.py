import random


class Coccinelle:
    def __init__(self, sexe, age, niv_nutrition):
        self.age = age
        self.esperance_de_vie = random.randint(200, 350)
        self.sexe = sexe
        self.niv_nutrition = niv_nutrition

    def chasser(self, nb_proies, nb_coccinelles):
        if nb_coccinelles == 0:
            return nb_proies

        proies_par_cocci = nb_proies / nb_coccinelles

        if proies_par_cocci > 20:
            consomme = random.randint(12, 20)
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)

        consomme = min(consomme, nb_proies)

        if consomme >= 10:
            self.niv_nutrition += 1
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1)

        return nb_proies - consomme

    def reproduction(self):
        """
        Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle.
        """
        descendants = []
        if self.sexe == "femelle" and self.niv_nutrition >= 2:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0

        return descendants

    def a_survecu(self):
        """
        Met à jour l'âge de la coccinelle et indique si elle est encore en vie.
        """
        self.age = self.age + 1
        return self.age < self.esperance_de_vie

    def __repr__(self):
        return f"Coccinelle {self.sexe}, âge: {self.age}/{self.esperance_de_vie}, niv_nutrition: {self.niv_nutrition}"


def evolution(population, nb_proies):
    """
    Simule une journée dans l'écosystème :
    - chasse des coccinelles
    - reproduction
    - vieillissement et mortalité
    - croissance des pucerons

    population est une liste d'instances de la classe Coccinelle
    nb_proies est un entier indiquant le nombre de proies

    Cette fonction renvoie un couple (population_suivante, nouveau_nb_proies) indiquant
    la nouvelle population à la fin de la journée et le nombre de proies.
    """
    population_suivante = []
    nouveau_nes = []
    nb_coccinelles = len(population)

    for coccinelle in population:
        nb_proies = coccinelle.chasser(nb_proies, nb_coccinelles)

        if coccinelle.a_survecu():
            population_suivante.append(coccinelle)

        nouveau_nes += coccinelle.reproduction()

    # Croissance naturelle des pucerons (augmentation de 20% par jour)
    nb_proies = int(nb_proies * 1.2)

    # Ajout des nouveau-nés en fin de journée
    population_suivante += nouveau_nes

    return population_suivante, nb_proies


#############################################################################
# Écrire ci-dessous le code pour les questions de l'énoncé                  #
#############################################################################


#EXO 1
a=Coccinelle("femelle",10,2)
b=Coccinelle("femmelle",10,2)
c=Coccinelle("male",10,2)
population= [a,b,c]
population_suivante, nb_proies=evolution(population,200)
for jour in range(5):
    population, nb_proies = evolution(population, nb_proies)
    print("Jour", jour, ":")
    print("  Coccinelles :", len(population))
    print("  Pucerons :", nb_proies)

#EXO 2

def simulation_simple(population, nb_proies):
    jour = 0
    while jour < 30 and len(population) > 0 and nb_proies > 0:
        population, nb_proies = evolution(population, nb_proies)
        jour += 1
    return (len(population), nb_proies, jour)

a = Coccinelle("femelle", 10, 2)
b = Coccinelle("femelle", 10, 2)
c = Coccinelle("male", 10, 2)
population = [a, b, c]
resultat = simulation_simple(population, 1000)
print(resultat)

#EXO 3

def chasser(self, nb_proies, nb_coccinelles):
    """
    Simule la chasse d'une coccinelle et met à jour son niveau de nutrition.
    :param nb_proies: (int) Le nombre total de proies disponibles
    :param nb_coccinelles: (int) Le nombre total de coccinelles
    :cu: nb_proies et nb_coccinelles doivent être des entiers positifs
    :return: (int) Le nombre de proies restantes après la chasse
    :exemples:
    >>> c = Coccinelle("femelle", 10, 2)
    >>> c.chasser(100, 5)
    <un entier <= 100>
    >>> c = Coccinelle("male", 10, 1)
    >>> c.chasser(0, 5)
    0
    >>> c = Coccinelle("femelle", 10, 2)
    >>> c.chasser(50, 0)
    50
    >>> c = Coccinelle("male", 10, 2)
    >>> c.chasser("100", 5)
    Traceback (most recent call last):
    ...
    AssertionError: nb_proies doit être un entier
    >>> c = Coccinelle("male", 10, 2)
    >>> c.chasser(-10, 5)
    Traceback (most recent call last):
    ...
    AssertionError: nb_proies doit être positif
    >>> c = Coccinelle("male", 10, 2)
    >>> c.chasser(50, -3)
    Traceback (most recent call last):
    ...
    AssertionError: nb_coccinelles doit être positif
    """
    assert isinstance(nb_proies, int), "nb_proies doit être un entier"
    assert isinstance(nb_coccinelles, int), "nb_coccinelles doit être un entier"
    assert nb_proies >= 0, "nb_proies doit être positif"
    assert nb_coccinelles >= 0, "nb_coccinelles doit être positif"
    if nb_coccinelles == 0:
        return nb_proies
        proies_par_cocci = nb_proies / nb_coccinelles
        if proies_par_cocci > 20:
            consomme = random.randint(12, 20)
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)
        consomme = min(consomme, nb_proies)
        if consomme >= 10:
            self.niv_nutrition += 1
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1)
        return nb_proies - consomme

#EXO 4

def reproduction(self):
        """
        Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle.
        """
        descendants = []
        if self.sexe == "femelle" and self.niv_nutrition >= 2 and self.age >= 20:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0
        return descendants

def a_survecu(self):
        """
        Met à jour l'âge de la coccinelle et indique si elle est encore en vie.
        """
        self.age += 1
        if self.age >= self.esperance_de_vie:
            return False
        if self.niv_nutrition == 0:
            if random.random() < 1/3:
                return False
        return True