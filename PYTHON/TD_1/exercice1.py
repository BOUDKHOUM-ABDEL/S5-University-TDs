
# �crire un programme qui : 
# 1. Cr�e une liste de nombres entiers saisis par l�utilisateur. 

my_list = []
length = 5
for index in range(length):
    number = int(input(f"Enter the {index+1}th number : "))
    my_list.append(number)
print(my_list)
    
# 2. Affiche : 
# o Liste triee sans utiliser sort() ni sorted():
for i in range(length):
    for j in range(i+1,length):
        if my_list[i] > my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[i]
            my_list[i] = temp
print(my_list)
    
# o Deuxieme plus grand element:
index =length -1
if my_list[0] == my_list[index]:
    print("not found, all numbers are simillar")

else:
   while my_list[index] == my_list[index-1]:
    index=index-1
    print(my_list[index-1])

# o Somme des elements aux indices pairs:
total = 0
for index in range(0,length,2):
        total+=my_list[index]
print(f"1.la Somme des elements aux indices pairs  :{total}")


# o Nouvelle liste contenant uniquement les valeurs uniques (sans utiliser set()):
unique_list = []
for number in my_list:
    if not number in unique_list:
       unique_list.append(number)
print(unique_list)
# 3. Remplace dans la liste tous les elements negatifs par 0:
for index in range(length):
    if my_list[index] < 0 :
      my_list[index] = 0
print(my_list)