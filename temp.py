from Personne import Personne
from voiture import Voiture
from avion import Avion

f = lambda x,y: x**2+y
print(f(3, 5))


def e_potentielle(masse, hauteur,e_limite, g=9.81):
    E = masse*hauteur*g
    print(E)
    return (E>e_limite)
    
print("Bonjour")
result = e_potentielle(80,5,3000)
print(result)

x=-1
if x>0:
    print(x,"positif")
elif x==0:
    print(x,"nul")    
else :
    print(x,"negatif")
    
    
#P = Personne("TOTO","Titi",14)
#P.__nom="titi"
#print(P.nom)
#P._Personne__nom = "TATA"
#print(P.nom)
#P.nom="aazeaze" 
##print(P.GetPersonn())
##help(P)
#
#print(P.nom)
list =[]
    
    
v1 = Voiture("520i","BMW", 58, 130)
v2 = Avion("F22","Raptor",2400,"missiles")

v3 = Voiture("Astra","Opel", 54, 130)
v4 = Avion("F16","Falcon",2400,"missiles")

v5 = Voiture("Cayen","Porshe", 50, 130)
v6 = Avion("F18","Hornet",2400,"missiles")

list.append(v1)
list.append(v2)
list.append(v3)
list.append(v4)
list.append(v5)
list.append(v6)

for item in list:
    print(item.get_info())
    
