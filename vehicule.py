class Vehicule:
    
    __nom = None
    __marque = None
    __quantite_essence = 0
    
    def __init__(self, nom, marque, quantite_essence):
        self.__nom = nom
        self.__marque = marque
        self.__quantite_essence = quantite_essence

    def get_info(self):
        return("{0} {1} {2} litres d'essences".format(
                self.__nom,self.__marque,self.__quantite_essence))
        