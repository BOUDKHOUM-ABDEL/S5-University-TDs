# Exercice 4 :
# 1. Écrire une fonction est_palindrome(chaine) qui retourne un booléen.
def est_palindrome(chaine):
    cleaned = ''.join(c.lower() for c in chaine if c.isalnum())
    return cleaned == cleaned[::-1]

# 2. Écrire une fonction sont_anagrammes(mot1, mot2) qui retourne un booléen.
def sont_anagrammes(mot1, mot2):
    from collections import Counter
    m1 = ''.join(c.lower() for c in mot1 if c.isalnum())
    m2 = ''.join(c.lower() for c in mot2 if c.isalnum())
    return Counter(m1) == Counter(m2)

# 3. Écrire une fonction groupes_anagrammes(liste_mots) qui regroupe les mots anagrammes.
def groupes_anagrammes(liste_mots):
    groupes = {}
    for mot in liste_mots:
        cle = ''.join(sorted(''.join(c.lower() for c in mot if c.isalnum())))
        if cle not in groupes:
            groupes[cle] = []
        groupes[cle].append(mot)
    return list(groupes.values())

# Tests
if __name__ == "__main__":
    print(est_palindrome("radar"))
    print(est_palindrome("Kyak"))
    print(sont_anagrammes("gare", "rage"))
    print(groupes_anagrammes(["gare", "rage", "chien", "niche", "chat"]))
