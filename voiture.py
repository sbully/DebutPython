from vehicule import Vehicule

class Voiture(Vehicule):
    
    def __init__(self, nom, marque, quantite_essence, puissance):
        Vehicule.__init__(self,nom,marque,quantite_essence)
        self.__puissance=puissance