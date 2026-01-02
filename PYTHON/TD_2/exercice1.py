

phrase = input("Write a sentence : ")

def analyse_text(text  , ignore_words =False) :
    articles = {"le", "la", "les", "de", "du", "des", "et", "à", "un", "une", "en"}
    words = text.lower().split()
    if ignore_words:
        words = [word for word in words if not articles]
    
    nb_words = len(words)
    max_word = max(words ,key= len) if words else ""

    f= {}
    for word in words :
       f[word] = f.get(word , 0) + 1

    return nb_words , max_word , f




nb_words , max_word , f = analyse_text(phrase)

print("\nAnalyse du texte :")
print(f"Nombre total de mots : {nb_words}")
print(f"Mot le plus long : {max_word}")
print("Fréquences des mots :")
for word, freq in f.items():
    print(f"{word:<10} : {freq}")