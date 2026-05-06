import csv
import math

class Renard:
    """
    Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee.
    """
    def __init__(self, identifiant, nom, poids, date_arrivee):
        self.identifiant = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self):
        return "Renard ID " + str(self.identifiant) + " - " + self.nom + " (Arrivé le " + self.date_arrivee + ")"
        

class Refuge:
    """
    Classe représentant le refuge contenant la liste des renards.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_renards = []
        
    def recueillir(self, un_renard):
        """
        Méthode d'ajout d'un renard au refuge.
        """
        self.liste_renards.append(un_renard)

    def lister_peu_corpulents(self):
        """
        Méthode qui renvoie une liste des Renards dont le poids est < 6.0 kg.
        """
        return [renard for renard in self.liste_renards if renard.poids < 6.0]

    def pourcentage_peu_corpulents(self):
        """
        Méthode qui renvoie le pourcentage des renards peu corpulents.
        """
        if len(self.liste_renards) == 0:
            return 0.0
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100

    def importer_donnees(self, nom_fichier):
        """
        Fonction qui importe les données des renards à partir d'un fichier CSV.
        """
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                renard = Renard(
                    int(ligne['id']),          
                    ligne['nom'],
                    float(ligne['poids']),    
                    ligne['date_arrivee']
                )
                self.recueillir(renard)
refuge = Refuge("SOS Goupil", "123 rue de la forêt")
refuge.importer_donnees("donnees_renards.csv")



peu_corpulents = refuge.lister_peu_corpulents()
print(peu_corpulents)

print(refuge.pourcentage_peu_corpulents())

nb_peu_corpulents = len(refuge.lister_peu_corpulents())
nb_total = len(refuge.liste_renards)
print(nb_peu_corpulents)  
print(nb_total)           

