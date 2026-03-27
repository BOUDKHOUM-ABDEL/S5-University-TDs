# Exercice 6 :
# On dispose de trois ensembles
maths = {"Ali", "Sara", "Mounir", "Yassine"}
physique = {"Sara", "Amine", "Yassine"}
informatique = {"Ali", "Yassine", "Amal"}

# 1. etudiants_communs(*ensembles)
def etudiants_communs(*ensembles):
    if not ensembles:
        return set()
    resultat = set(ensembles[0])
    for e in ensembles[1:]:
        resultat &= set(e)
    return resultat

# 2. etudiants_uniques(*ensembles)
def etudiants_uniques(*ensembles):
    # Les étudiants inscrits dans une seule matière
    tous_les_etudiants = {}
    for e in ensembles:
        for etudiant in e:
            tous_les_etudiants[etudiant] = tous_les_etudiants.get(etudiant, 0) + 1
    
    uniques = {etudiant for etudiant, compte in tous_les_etudiants.items() if compte == 1}
    return uniques

# 3. statistiques_groupes()
def statistiques_groupes():
    print(f"Nombre d'étudiants en Maths: {len(maths)}")
    print(f"Nombre d'étudiants en Physique: {len(physique)}")
    print(f"Nombre d'étudiants en Informatique: {len(informatique)}")
    
    tous = maths | physique | informatique
    print(f"Total des étudiants uniques: {len(tous)}")

# Tests
if __name__ == "__main__":
    print("Étudiants communs aux 3 matières:", etudiants_communs(maths, physique, informatique))
    print("Étudiants inscrits dans une seule matière:", etudiants_uniques(maths, physique, informatique))
    print("\nStatistiques:")
    statistiques_groupes()
