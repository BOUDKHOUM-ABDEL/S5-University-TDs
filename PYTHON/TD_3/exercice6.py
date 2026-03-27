import itertools

# 5. Décorateur journalise_gen
def journalise_gen(gen_func):
    def wrapper(*args, **kwargs):
        gen = gen_func(*args, **kwargs)
        for valeur in gen:
            print(f"[Journal] Production de la valeur: {valeur}")
            yield valeur
    return wrapper

# 1. Générateur pairs(n)
@journalise_gen
def pairs(n):
    for i in range(0, n + 1, 2):
        yield i

# 2. Générateur entiers() (suite infinie)
def entiers():
    n = 1
    while True:
        yield n
        n += 1

# 3. Générateur carres(gen)
def carres(gen):
    for val in gen:
        yield val * val

# Test
if __name__ == "__main__":
    print("--- 1. Nombres pairs jusqu'à 10 ---")
    list(pairs(10)) # Consommer le générateur pour voir les logs
    
    print("\n--- 4. Les 10 premiers carrés d'entiers ---")
    gen_entiers = entiers()
    gen_carres = carres(gen_entiers)
    
    dix_premiers = list(itertools.islice(gen_carres, 10))
    print(dix_premiers)
