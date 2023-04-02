class forme () : 

    def aire (self) :
        return 0

class rectangle(forme) :

    def __init__(self, largeur, hauteur) : 
        self.hauteur = hauteur 
        self.largeur = largeur 
    
    def aire(self) : 
        return self.hauteur * self.largeur

rectangle = rectangle(10, 10)
aire_rectangle = rectangle.aire()

print("L'aire du rectangle est : ", aire_rectangle)

class Cercle(forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return self.radius
    
Cercle = Cercle (10)
Cercle.aire ()


