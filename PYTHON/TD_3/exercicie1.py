def compteur():
    n = 0  # variable locale, "capturée" par la sous-fonction

    def incremente():
        nonlocal n  # indique que n appartient à la portée fermée
        n += 1
        return n

    return incremente


# Test du comportement :
c1 = compteur()
c2 = compteur()
print(c1(), c1(), c2(), c1(), c2())
# => sortie attendue : 1 2 1 3 2