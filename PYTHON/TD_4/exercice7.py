from abc import ABC, abstractmethod

# Exercice 7 : Classes Abstraites

class Employe(ABC):
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    @abstractmethod
    def calculer_salaire(self):
        pass

    def description(self):
        return f"{self.nom} ({self.age} ans) - Salaire: {self.calculer_salaire()} MAD"

class EmployeHoraire(Employe):
    def __init__(self, nom, age, taux_horaire, heures):
        super().__init__(nom, age)
        self.taux_horaire = taux_horaire
        self.heures = heures

    def calculer_salaire(self):
        return self.taux_horaire * self.heures

class EmployeMensuel(Employe):
    def __init__(self, nom, age, salaire_fixe):
        super().__init__(nom, age)
        self.salaire_fixe = salaire_fixe

    def calculer_salaire(self):
        return self.salaire_fixe

# Tests
if __name__ == "__main__":
    employes = [
        EmployeHoraire("Alice", 25, 100, 160),
        EmployeMensuel("Bob", 35, 20000),
        EmployeHoraire("Charlie", 22, 120, 80)
    ]
    
    for emp in employes:
        print(emp.description())
