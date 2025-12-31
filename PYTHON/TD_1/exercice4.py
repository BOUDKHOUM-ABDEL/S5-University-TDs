# Exercice 4 : 
# 1. Saisir deux ensembles de nombres (par exemple A et B):

# 2. Afficher : 
# o Eléments communs (intersection):
# o Eléments uniques à A et à B, 
# o Eléments pairs dans l’union des deux ensembles, 
# o Eléments présents dans un seul ensemble. 
# 3. Construire un nouvel ensemble contenant les carrés de tous les nombres présents dans 
# A ∪ B.
# 1. Saisir deux ensembles de nombres
a_input = input("Entrez les éléments de l'ensemble A séparés par des espaces : ")
b_input = input("Entrez les éléments de l'ensemble B séparés par des espaces : ")

# Convertir les chaînes en listes de nombres
def convertir_en_liste(chaine):
    liste = []
    nombre = ""
    for char in chaine:
        if char != " ":
            nombre += char
        else:
            if nombre != "":
                liste.append(int(nombre))
                nombre = ""
    if nombre != "":
        liste.append(int(nombre))
    return liste

A = convertir_en_liste(a_input)
B = convertir_en_liste(b_input)

# Supprimer les doublons manuellement
def supprimer_doublons(liste):
    unique = []
    for x in liste:
        if x not in unique:
            unique.append(x)
    return unique

A = supprimer_doublons(A)
B = supprimer_doublons(B)

# 2.a Éléments communs (intersection)
intersection = []
for x in A:
    if x in B and x not in intersection:
        intersection.append(x)

# 2.b Éléments uniques à A et à B
uniques_A = []
for x in A:
    if x not in B:
        uniques_A.append(x)

uniques_B = []
for x in B:
    if x not in A:
        uniques_B.append(x)

# 2.c Éléments pairs dans l’union
union = A[:]
for x in B:
    if x not in union:
        union.append(x)

pairs = []
for x in union:
    if x % 2 == 0:
        pairs.append(x)

# 2.d Éléments présents dans un seul ensemble
uniques_total = []
for x in A:
    if x not in B:
        uniques_total.append(x)
for x in B:
    if x not in A:
        uniques_total.append(x)

# 3. Ensemble des carrés de A ∪ B
carres = []
for x in union:
    carres.append(x * x)

# Affichage des résultats
print("\n--- Résultats ---")
print("A :", A)
print("B :", B)
print("Intersection :", intersection)
print("Uniquement dans A :", uniques_A)
print("Uniquement dans B :", uniques_B)
print("Éléments pairs dans A ∪ B :", pairs)
print("Éléments présents dans un seul ensemble :", uniques_total)
print("Carrés des éléments de A ∪ B :", carres)