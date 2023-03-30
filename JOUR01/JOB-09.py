class Student () : 
    def __init__(self, nom= "Doe", prenom= "John", numero=145, credit=0) :
        self._nom = nom
        self._prenom = prenom
        self._numero = numero
        self._credit = credit

    def  add_credit (self) : 
         self._credit = 10 
         self._credit += 10
         self._credit += 50
         self._numero = 145 
         print ("Nom = ", self._nom)
         print ( "Prenom=", self._prenom,)
         print ("id=", self._numero)
         if isinstance (self._credit, int) <= 0 :
             exit
        
    def _StudentEval (self) : 
        if (self._credit) <=70 : 
            print ("Niveau = Bien")




Student = Student ()

Student.add_credit ()
Student._StudentEval ()
