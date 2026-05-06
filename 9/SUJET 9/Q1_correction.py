import math


class Sommet:

    """
    Représente un sommet (point) dans l'espace 3D.
    """

    def __init__(self, x, y, z):
        """
        Initialise un sommet avec ses coordonnées.
        """
        self.x = x
        self.y = y
        self.z = z

    def est_adjacent(self, sommet):
        """
        Indique si le sommet courant est adjacent à un autre sommet.
        """
        nb_changement = 0
        if self.x != sommet.x:
            nb_changement += 1
        if self.y != sommet.y:
            nb_changement += 1
        if self.z != sommet.z:
            nb_changement += 1
        return nb_changement == 1


#############################################################################
# Écrire le code de la méthode distance de la question 1
    def distance(self,sommet):
        """
        renvoie la distance entre l'objet courant et sommet
        :param sommet: (Sommet) sommet
        :return: (int) renvoie la distance entre l'objet courant et sommet
        """
        assert isinstance(sommet,Sommet), "doit etre un sommet"
        d_x = self.x - sommet.x
        d_y = self.y - sommet.y
        d_z = self.z - sommet.z
        return math.sqrt(d_x**2 + d_y**2 + d_z**2)
#############################################################################

#############################################################################
# Programme pour tester votre méthode de la question 1                                  #
#############################################################################

if __name__ == "__main__":
    s1 = Sommet(0, 0, 0)
    s2 = Sommet(3, 4, 0)
    
    #QUESTION 1
    print(s1.distance(s2))
