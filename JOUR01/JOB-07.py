class Livre () :
    def __init__(self, titre, auteur, pages) :
         self.__titre = titre 
         self.__auteur = auteur 
         self.__pages = pages
    
    def get_titre (self) :
         return self.__titre 
    def set_titre (self, titre) :
         self.__titre = titre

    def get_auteur(self) :
         return self.__auteur
    def set_auteur(self, auteur) :
         self.__auteur = auteur

    def get_pages (self) :
         return self.__pages 

    def set_pages (self, pages) :
         if isinstance (pages, int) and pages > 0 : 
                self.__pages = pages
         else : print ("Erreur")

livre = Livre ("Titre : Don Quichotte", "Auteur : Miguel de Cervantes", 43)

print (livre.get_auteur())
print (livre.get_titre())
print (livre.get_pages())


 
        