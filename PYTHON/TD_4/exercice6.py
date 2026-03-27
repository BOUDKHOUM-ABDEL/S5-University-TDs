import math

# Exercice 6 : Surcharge des opérateurs

class Vecteur2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"

    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

# Tests
if __name__ == "__main__":
    v1 = Vecteur2D(3, 4)
    v2 = Vecteur2D(1, 2)
    
    print("v1 =", v1)
    print("v2 =", v2)
    print("Somme :", v1 + v2)
    print("Différence :", v1 - v2)
    print("Égalité v1 == v2 :", v1 == v2)
    print("Norme de v1 :", v1.norme())
