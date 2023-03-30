class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)

personne1 = Personne("Jean", "Doe")
personne2 = Personne("Jean", "Dupond")


personne1.SePresenter()
personne2.SePresenter()

