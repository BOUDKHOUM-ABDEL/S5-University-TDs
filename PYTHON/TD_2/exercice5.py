classement = { 
    "Equipe A": {"victoires": 5, "defaites": 2, "nuls": 1}, 
    "Equipe B": {"victoires": 4, "defaites": 1, "nuls": 3}, 
    "Equipe c": {"victoires": 5, "defaites": 0, "nuls": 3},
    "Equipe D": {"victoires": 1, "defaites": 6, "nuls": 3},
    "Equipe E": {"victoires": 3, "defaites": 2, "nuls": 3},
    "Equipe F": {"victoires": 7, "defaites": 1, "nuls": 0},
    "Equipe G": {"victoires": 4, "defaites": 4, "nuls": 0},
    "Equipe H": {"victoires": 3, "defaites": 5, "nuls": 0}
}

def calcul_points(equipe):
    return equipe["victoires"] * 3 + equipe["nuls"]

def trier_classement(classement):
    return sorted(classement.items(), key=lambda e: calcul_points(e[1]), reverse=True)

def meilleure_equipe(classement):
    equipe = trier_classement(classement)[0]
    return equipe


print(trier_classement(classement))
print("Classement trié :")
for nom, stats in trier_classement(classement):
    print(f"{nom:<10}  Points: {calcul_points(stats)}")

print("\nMeilleure équipe :", meilleure_equipe(classement))