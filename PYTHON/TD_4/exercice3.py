class Forme:
    def surface(self):
        return 0

    def description(self):
        return "Forme géométrique"


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur

    def description(self):
        return "Rectangle"


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        from math import pi
        return pi * self.rayon ** 2

    def description(self):
        return "Cercle"


if __name__ == "__main__":
    formes = [Rectangle(4, 2), Cercle(3), Forme()]
    for f in formes:
        print(f"{f.description()} : Surface = {f.surface():.2f}")
