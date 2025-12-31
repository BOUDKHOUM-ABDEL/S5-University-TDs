# 1. Liste de tuples
etudiants = [("Ali", 15), ("Sara", 18), ("Nadia", 12), ("Youssef", 17)]

# 2a. Construire le dictionnaire notes
notes = {nom: note for nom, note in etudiants}

# 2b. Construire l'ensemble des étudiants avec note ≥ 15
admis = {nom for nom, note in etudiants if note >= 15}

# 2c. Construire la liste triée des noms par note décroissante (sans sorted)
# On utilise un tri par sélection manuel
etudiants_copy = etudiants[:]  # copie pour ne pas modifier l'original
for i in range(len(etudiants_copy)):
    max_index = i
    for j in range(i+1, len(etudiants_copy)):
        if etudiants_copy[j][1] > etudiants_copy[max_index][1]:
            max_index = j
    # Échanger
    etudiants_copy[i], etudiants_copy[max_index] = etudiants_copy[max_index], etudiants_copy[i]

# Extraire uniquement les noms dans l'ordre décroissant
noms_trie_desc = [nom for nom, note in etudiants_copy]

# 3. Afficher les structures
print("Dictionnaire des notes :", notes)
print("Étudiants avec note ≥ 15 :", admis)
print("Noms triés par note décroissante :", noms_trie_desc)