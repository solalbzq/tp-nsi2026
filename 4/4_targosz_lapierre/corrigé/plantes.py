class Plante:
    def __init__(self, nom, espece, duree_croissance, taille_moyenne, exposition):
        self.nom = nom
        self.espece = espece
        self.duree_croissance = duree_croissance  # en jours
        self.taille_moyenne = taille_moyenne      # en cm
        self.exposition = exposition              # "ombre", "mi-ombre", "plein soleil"



# Liste des plantes étudiées
plantes = [
    Plante("plante1", "tomate", 60, 150, "plein soleil"),
    Plante("plante2", "laitue", 45, 30, "mi-ombre"),
    Plante("plante3", "basilic", 30, 40, "plein soleil"),
    Plante("plante4", "menthe", 50, 60, "ombre"),
]