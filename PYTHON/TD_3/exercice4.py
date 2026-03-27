# Exercice 4 :
# 1. Créez une fonction appliquer(f, L) qui applique f à chaque élément de L.
def appliquer(f, L):
    return [f(x) for x in L]

# 2. Créez une fonction compose(f, g) qui retourne f(g(x)).
def compose(f, g):
    def h(x):
        return f(g(x))
    return h

# 3. Testez avec
def double(x):
    return 2 * x

def carre(x):
    return x * x

if __name__ == "__main__":
    h = compose(carre, double)
    print(h(5))  # Résultat attendu : 100
    
    L = [1, 2, 3]
    print(appliquer(double, L))
