class Personne:
    """
    Classe Personne
    """
    __nom="" 
    __prenom=""
    __age=0
    

    
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age=age
        
    def GetPersonn(self):
       return ('mon nom est: {0} et mon prenom {1}'.format(self.__nom,self.__prenom))
       #return ("mon nom est: %s %s" % (self.nom,self.prenom))

    #getter
    def _getage(self):
        try:
            return self.__nom
        except AttributeError:
            print("le nom n existe pas")
    #setter
    def _setage(self, newnom):
        if self.__nom != newnom :
            self.__nom= newnom
    #suppression d attribut    
    def _delage(self):
        del self.__nom
        

    
        #property(<getter>,<setter>,<deleter>,<helper>)
    nom= property(_getage, _setage, _delage, "Nom de la personne")