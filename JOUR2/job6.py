class Vehicule () : 

    def __init__(self, marque, annee, prix) : 
        self.marque = marque 
        self.annee = annee
        self.prix = prix 

    def InformationVehicule (self,modele) : 
        print ()
        print ("Marque :", self.marque)
        print ("Modele :",modele)
        print ("Année :",self.annee)
        print ("Prix :",self.prix)

    def Demmarrer (self) : 
        print ("Attention, je roule")

class Voiture(Vehicule) :

    def __init__(self, marque, annee, prix, portes = 4):
        super().__init__(marque, annee, prix)
        self.portes = portes
         
    def InformationVehicule(self, modele):
        return super().InformationVehicule(modele)
    
    
    def Demmarrer (self) : 
        print ("Attention, je vais faire vroum vroum")

voiture = Voiture ("Mercedes",2020,18500,)
voiture.InformationVehicule ("Class A")
ndp = voiture.portes
print ("Nombre de porte :",ndp)
voiture.Demmarrer ()

class Moto(Vehicule) :

    def __init__(self, marque, annee, prix, roue = 4):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def InformationVehicule(self, modele):
        return super().InformationVehicule(modele)
       
    def Demmarrer (self) : 
        print ("Attention, je roule avec mon vmax")

    
moto = Moto ("Yamaha",1987,4500)
moto.InformationVehicule ("1200 Vmax")
Roue = moto.roue
print ("Nombre de roue :",Roue)
moto.Demmarrer ()


