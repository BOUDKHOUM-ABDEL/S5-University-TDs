# Exercice 4 : Héritage Multiple et MRO

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Nom : {self.nom}, Age : {self.age}")

class Employe(Personne):
    def __init__(self, nom, age, salaire, poste):
        super().__init__(nom, age)
        self.salaire = salaire
        self.poste = poste

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Poste : {self.poste}, Salaire : {self.salaire}")

class Formateur(Personne):
    def __init__(self, nom, age, matiere_enseignee):
        super().__init__(nom, age)
        self.matiere_enseignee = matiere_enseignee

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Matière enseignée : {self.matiere_enseignee}")

# Héritage Multiple
class FormateurPermanent(Employe, Formateur):
    def __init__(self, nom, age, salaire, poste, matiere_enseignee):
        # Initialisation manuelle pour éviter les conflits super() dans l'héritage diamant simple
        Personne.__init__(self, nom, age)
        self.salaire = salaire
        self.poste = poste
        self.matiere_enseignee = matiere_enseignee

    def afficher_infos(self):
        print("--- Informations Formateur Permanent ---")
        Personne.afficher_infos(self)
        print(f"Poste : {self.poste}, Salaire : {self.salaire}")
        print(f"Matière enseignée : {self.matiere_enseignee}")

# Tests
if __name__ == "__main__":
    fp = FormateurPermanent("Dr. Ahmed", 45, 15000, "Professeur HDR", "Informatique")
    fp.afficher_infos()
    print("\nOrdre de résolution des méthodes (MRO):")
    for cls in FormateurPermanent.__mro__:
        print(cls.__name__)
