import random
import itertools

# Décorateur affiche_etapes
def affiche_etapes(nom_etape):
    def decorateur(gen_func):
        def wrapper(*args, **kwargs):
            gen = gen_func(*args, **kwargs)
            for valeur in gen:
                print(f"[{nom_etape}] -> {valeur}")
                yield valeur
        return wrapper
    return decorateur

@affiche_etapes("1. Lecture")
def lecture_donnees():
    while True:
        yield random.randint(0, 100)

@affiche_etapes("2. Filtre Pair")
def filtre_pair(flux):
    for val in flux:
        if val % 2 == 0:
            yield val

@affiche_etapes("3. Normalisation (0-1)")
def normalise(flux):
    for val in flux:
        yield val / 100.0

if __name__ == "__main__":
    print("Traitement d'un flux de données :")
    
    # Construction du pipeline de données
    flux_brut = lecture_donnees()
    flux_filtre = filtre_pair(flux_brut)
    flux_normalise = normalise(flux_filtre)
    
    # Consommer les 10 premiers éléments valides
    resultats = list(itertools.islice(flux_normalise, 10))
    
    print("\nRésultats finaux :")
    print([round(v, 2) for v in resultats])
