from vehicule import Vehicule

class Avion(Vehicule):
    
    def __init__(self,nom,marque,essence,marchandise):
        Vehicule.__init__(self,nom,marque,essence)
        self.__marchandise=marchandise