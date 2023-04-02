class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'age est :", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge
        print("Le nouvel age est", self.age, "ans")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self,  matiereEnseignee="Math"):
        super().__init__(age=40)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


personne = Personne()
personne.afficherAge()
personne.bonjour()
personne.modifierAge(20)

eleve = Eleve()
eleve.bonjour() 
eleve.allerEnCours() 
eleve.affichageAge ()

professeur = Professeur ()
professeur.bonjour()
professeur.afficherAge ()
professeur.enseigner()