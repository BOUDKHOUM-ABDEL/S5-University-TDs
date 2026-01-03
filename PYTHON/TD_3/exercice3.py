

# --- A. Somme des chiffres ---
def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)

print("Somme des chiffres de 1234 :", somme_chiffres(1235454354))

def pair(n):
    if n == 0:
        return True
    return impair(n - 1)

def impair(n):
    if n == 0:
        return False
    return pair(n - 1)

# Test
print("7 est pair ?", pair(7))
print("8 est pair ?", pair(8))