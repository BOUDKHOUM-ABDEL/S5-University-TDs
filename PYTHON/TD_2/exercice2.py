import math , random
def statistiques(liste):
    n = len(liste)
    moyenne = sum(liste)/n
    liste_triee = sorted(liste)
    mediane = liste_triee[n // 2] if n % 2 != 0 else (liste_triee[n//2 - 1] + liste_triee[n//2]) / 2
    ecart_type = math.sqrt(sum((x - moyenne) ** 2 for x in liste) / n)    
    return moyenne, mediane, min(liste), max(liste), ecart_type
def filtrer(liste, borne_min, borne_max):
    return [x for x in liste if borne_min <= x <= borne_max]

n = int(input("Combien de nombres générer ? "))
valeurs = [random.randint(0, 100) for _ in range(n)]
print("\nListe générée :", valeurs)

m, med, minv, maxv, ec = statistiques(valeurs)
print(f"\nMoyenne={m:.2f}, Médiane={med}, Min={minv}, Max={maxv}, Écart-type={ec:.2f}")

bornemin = int(input("\nFiltrer à partir de : "))
bornemax = int(input("Jusqu’à : "))
valeurs_filtrees = filtrer(valeurs, bornemin, bornemax)
print("Liste filtrée :", valeurs_filtrees)
