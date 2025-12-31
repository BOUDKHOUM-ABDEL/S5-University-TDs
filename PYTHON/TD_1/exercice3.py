# Exercice 3 : 
# Écrire un programme qui : 
# 1. Lit une phrase saisie par l’utilisateur:

phrase = input("Enter a sentences : ")

# 2. Affiche : 
# o Nombre de mots:
#-----------------------------------------------------
#mots = phrase.split()  # Sépare la phrase en mots
#nbr_word = len(mots)   # Compte le nombre de mots
#-----------------------------------------------------
nbr_word=1
for char in phrase :
    if char==" ":
        nbr_word +=1
print(nbr_word)

# o Mot le plus long et le plus court:
words = phrase.split()# Sépare la phrase en mots



           # Parcourir les mots pour trouver le plus long et le plus court
max_len = len(words[0])
min_len = len(words[0])

for w in words:
    if len(w) > max_len:
        max_len = len(w)
    if len(w) < min_len:
        min_len = len(w)

           # Collecter tous les mots qui ont cette longueur
longest_words = []
shortest_words = []

for w in words:
    if len(w) == max_len:
        longest_words.append(w)
    if len(w) == min_len:
        shortest_words.append(w)

print("Mots les plus longs :", longest_words)
print("Mots les plus courts :", shortest_words)


# o Fréquence de chaque lettre (sans collections.Counter): 

letters = [letter for letter in phrase.upper() if letter !=" "]

dic_letters =dict.fromkeys(set(letters),0)
for letter in letters:
    dic_letters[letter]+=1
for key,value in dic_letters.items():
    print(f"{key} : {value}")

# o Phrase inversée mot par mot (sans split() inversé directement):
phrase_inversee = ""
word = ""
words = []
length = len(phrase)
for letter in phrase :
    if letter != " ":
        word+=letter
        
    elif letter == " " :
        phrase_inversee=word +" "+phrase_inversee
        word = ""

print(word+" "+phrase_inversee)

# 3. Vérifie si la phrase est un pangramme (contient toutes les lettres de l’alphabet).

is_pangramme = True
letters = set(letters)

if len(letters)==26:
    print("La phrase est un pangramme.")
else:
    print("La phrase n'est pas un pangramme.")
