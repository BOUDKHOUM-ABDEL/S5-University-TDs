import time
import functools

# 1. Décorateur chrono
def chrono(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        resultat = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[Chrono] {func.__name__}({args}, {kwargs}) a pris {fin - debut:.6f} secondes")
        return resultat
    return wrapper

# 2. Décorateur memo cache
def memo(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# 3. Application des deux décorateurs à fibo(n)
@chrono
@memo
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

# Test
if __name__ == "__main__":
    print("-" * 30)
    print("Calcul fibo(5) avec @chrono puis @memo :")
    print("Resultat :", fibo(5))
    
    print("-" * 30)
    print("Calcul fibo(6) (utilise le cache pour 5) :")
    print("Resultat :", fibo(6))
