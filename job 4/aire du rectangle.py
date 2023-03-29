class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


rectangle1 = Rectangle(largeur=5, hauteur=3)

aire_rectangle1 = rectangle1.aire()

print("L'aire du rectangle est:", aire_rectangle1)
