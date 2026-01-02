
def ajouter_produit(inventaire, id, nom, prix, quantite):
    inventaire.append({"id": id, "nom": nom, "prix": prix, "quantite": quantite})

def supprimer_produit(inventaire, id):
    inventaire[:] = [p for p in inventaire if p["id"] != id]

def valeur_totale(inventaire):
    return sum(p["prix"] * p["quantite"] for p in inventaire)

def produits_en_rupture(inventaire):
    return [p for p in inventaire if p["quantite"] == 0]

def recherche(inventaire, mot_cle):
    mot_cle = mot_cle.lower()
    return [p for p in inventaire if mot_cle in p["nom"].lower()]

inventaire = []
ajouter_produit(inventaire, 1, "Clavier", 250.0, 10)
ajouter_produit(inventaire, 2, "Souris", 120.0, 0)
ajouter_produit(inventaire, 3, "Écran", 1300.0, 5)

print("Liste inventaire :", inventaire)

print("Valeur totale du stock :", valeur_totale(inventaire))
print("Produits en rupture :", produits_en_rupture(inventaire))
print("Recherche 'sour' :", recherche(inventaire, "sour"))
supprimer_produit(inventaire, 2)
print("Liste après suppression 'id=2' :", inventaire)
