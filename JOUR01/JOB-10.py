class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50
        
    def get_marque(self):
        return self._marque
    
    def set_marque(self, marque):
        self._marque = marque
    
    def get_modele(self):
        return self._modele
    
   
