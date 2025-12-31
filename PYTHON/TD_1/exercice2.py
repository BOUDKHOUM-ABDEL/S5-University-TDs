# Exercice 2 :  
# 1.Creer un tuple contenant des entiers et des chaines. 
my_tuple = ("Aura",1,3,5,"Camilia",2,"Aura","Bostan")
print(my_tuple)
# 2. Tenter de modifier un element et observer le message d'erreur. 
# 3. Construire un nouveau tuple issu du precrdent mais : 
# o Sans doublons:
unique_tuple = tuple(set(my_tuple))
print(unique_tuple)
#  Trie selon la longueur des elements (pour les chaines):
chaines = [x for x in unique_tuple if isinstance(x, str)]
entiers = [x for x in unique_tuple if isinstance(x, int)]

chaines_triees = sorted(chaines, key=len)

nouveau_tuple = tuple(entiers + chaines_triees)
print(nouveau_tuple)




# 4. Convertir ce tuple en liste, inserer un nouvel element au milieu, puis reconvertir en 
# tuple.

ma_liste = list(nouveau_tuple)

# Calculer la position du milieu
milieu = len(ma_liste) // 2

# Insérer un nouvel élément
ma_liste.insert(milieu, "lion")

# Reconvertir en tuple
final_tuple = tuple(ma_liste)
print(final_tuple)