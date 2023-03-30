class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre 
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages 

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0: 
            self.__pages = pages
        else: 
            print("Erreur")

    def verification(self):
        return self.__disponible 
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            return True
        else:
            return False
    
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True

livre = Livre("Don Quichotte", "Miguel de Cervantes", 406)
print(livre.get_auteur())
print(livre.get_titre())
print(livre.get_pages())
print(livre.verification())

if livre.emprunter():
    print("Le livre a été emprunté.")
else:
    print("Le livre n'est pas disponible.")

livre.rendre()
print(livre.verification())
