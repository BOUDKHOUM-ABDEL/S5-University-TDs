# 1. Saisie des paires nom:note
# On demande à l'utilisateur de saisir plusieurs étudiants
# Exemple de saisie : "Ali 15", "Sara 18", "Omar 12"
# On arrête avec une chaîne vide

from typing import Dict

notes_dict: Dict[str, float] = {}
while True:
    entree = input("Entrez nom et note (ou vide pour finir) : ")
    if entree == "":
        break
    try:
        nom, note = entree.split()
        note = float(note)  # conversion en nombre
        notes_dict[nom] = note
    except ValueError:
        print("Format incorrect. Exemple : Ali 15")

print("\nDictionnaire initial :", notes_dict)

# 2. Calcul de la moyenne
moyenne = sum(notes_dict.values()) / len(notes_dict)
print("Moyenne des notes :", moyenne)

# 3a. Trouver la meilleure note
meilleure_note = max(notes_dict.values())
etudiants_meilleurs = [nom for nom, note in notes_dict.items() if note == meilleure_note]
print("Étudiants avec la meilleure note :", etudiants_meilleurs)

# 3b. Trier par note décroissante (sans sorted)
# On utilise une boucle pour construire une liste triée manuellement
notes_items = list(notes_dict.items())

# Tri par sélection (descendant)
for i in range(len(notes_items)):
    max_index = i
    for j in range(i+1, len(notes_items)):
        if notes_items[j][1] > notes_items[max_index][1]:
            max_index = j
    # Échanger
    notes_items[i], notes_items[max_index] = notes_items[max_index], notes_items[i]

print("Liste triée par note décroissante :", notes_items)

# 4. Supprimer les entrées < moyenne
notes_dict = {nom: note for nom, note in notes_dict.items() if note >= moyenne}
print("Dictionnaire après suppression (< moyenne) :", notes_dict)