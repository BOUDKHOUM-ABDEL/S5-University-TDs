

etudiants = [("Ali", 14), ("Sara", 18), ("Youssef", 11), ("Nada", 19), ("Khalid", 14)]


etudiants_tries = sorted(etudiants, key=lambda e: (e[1], e[0]))
print("Étudiants triés :", etudiants_tries)

# 2. Filtrage des étudiants au-dessus de la moyenne
moyenne = sum(note for _, note in etudiants) / len(etudiants)
admis = list(filter(lambda e: e[1] > moyenne, etudiants))
print("Étudiants au-dessus de la moyenne :", admis)

# 3. Transformation en mentions
def mention(note):
    if note < 12:
        return "Insuffisant"
    elif note < 16:
        return "Passable"
    elif note < 18:
        return "Bien"
    else:
        return "Très bien"

mentions = list(map(lambda e: (e[0], mention(e[1])), etudiants))
print("Mentions attribuées :", mentions)