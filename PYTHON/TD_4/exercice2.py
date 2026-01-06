

class CompteBancaire:
    def __init__(self, titulaire, solde=0.0, devise="MAD"):
        self.__titulaire = titulaire
        self.__solde = solde
        self.__devise = devise

    @property
    def solde(self):
        return self.__solde

    @solde.setter
    def solde(self, montant):
        if montant >= 0:
            self.__solde = montant
        else:
            print("Erreur : solde négatif interdit.")

    @property
    def devise(self):
        return self.__devise

    @devise.setter
    def devise(self, valeur):
        if valeur in ["MAD", "USD", "EUR"]:
            self.__devise = valeur
        else:
            print("Erreur : devise non autorisée.")

    def afficher(self):
        print(f"{self.__titulaire} : {self.__solde} {self.__devise}")


if __name__ == "__main__":
    c = CompteBancaire("Sara", 500)
    c.afficher()
    c.solde = -100  # Test d'encapsulation
    c.devise = "GBP"  # Devise non autorisée
    c.afficher()
