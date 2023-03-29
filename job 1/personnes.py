class Person:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifier_age(self, new_age):
        self.age = new_age


class Eleve(Person):
    def __init__(self, age):
        super().__init__(age)

    def aller_en_cours(self):
        print("Je vais en cours")

    def affichage_age(self):
        print("J'ai", self.age, "ans")


class Professeur(Person):
    def __init__(self, age, matiere_enseignee):
        super().__init__(age)
        self.matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")


eleve1 = Eleve(16)
person1 = Person()


person1.modifier_age(38)
person1.afficher_age()
person1.bonjour()

eleve1.aller_en_cours()
eleve1.afficher_age()
eleve1.affichage_age()

prof1 = Professeur(45, "mathématiques")
prof1.enseigner()