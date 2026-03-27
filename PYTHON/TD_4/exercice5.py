import math

# Implémentation basique des formes pour l'itérateur
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
        return math.pi * self.rayon ** 2
        
    def description(self):
        return "Cercle"

# Exercice 5 : La Collection de Formes
class CollectionFormes:
    def __init__(self):
        self._formes = []
        self._index = 0

    def ajouter(self, forme: Forme):
        self._formes.append(forme)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._formes):
            forme = self._formes[self._index]
            self._index += 1
            return forme
        else:
            raise StopIteration

# Test
if __name__ == "__main__":
    collection = CollectionFormes()
    collection.ajouter(Rectangle(5, 3))
    collection.ajouter(Cercle(4))
    
    print("--- Affichage du polymorphisme depuis de la collection itérable ---")
    for forme in collection:
        print(f"{forme.description()} - Surface: {forme.surface():.2f}")
