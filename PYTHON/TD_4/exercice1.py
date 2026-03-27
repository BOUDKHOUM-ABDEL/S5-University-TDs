class CompteBancaire:
  
    def __init__(self, titulaire, solde=0.0, devise="MAD"):
        self.titulaire = titulaire
        self.solde = solde
        self.devise = devise

    def deposer(self, montant):
        """Ajoute un montant au solde."""
        if montant > 0:
            self.solde += montant
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        """Retire un montant si le solde est suffisant."""
        if 0 < montant <= self.solde:
            self.solde -= montant
        else:
            print("Opération refusée : solde insuffisant.")

    def afficher_solde(self):
        """Affiche le solde actuel."""
        print(f"Compte de {self.titulaire} : {self.solde} {self.devise}")


class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.comptes = []  # Composition

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher_comptes(self):
        print(f"Comptes du client {self.prenom} {self.nom}:")
        for c in self.comptes:
            c.afficher_solde()


#  *** Exemple d'utilisation ***
#   Quand Python exécute un fichier, il crée automatiquement une variable 
#   spéciale : __name__
#       - Si le fichier est exécuté directement, alors :__name__ == "__main__"
#       - Si le fichier est importé, alors : __name__ == "nom_du_module"

if __name__ == "__main__":
    c1 = CompteBancaire("Ahmed", 15000)
    c2 = CompteBancaire("Ahmed", 3000, "EUR")

    client = Client("El Mansouri", "Ahmed")
    client.ajouter_compte(c1)
    client.ajouter_compte(c2)
    client.afficher_comptes()