name_list = ['Leo', 'Lucas', 'Laurent']
# Trouver l'indice(index) d'un élément
print(name_list.index("Laurent"))
# Insertion d'un élément
name_list.insert(1, 'Kevin')
print(name_list)
print("-----------")

my_list = [1, 2, 3]
# Modifier la valeur d'un élément à une position spécifique(index)
my_list[0] = 5
print(my_list)

my_list2 = [1, 2, 3]
# Ajouter un élément
my_list2.append(4)
print(my_list2)

my_list3= [1, 2, 3]
my_list3.append([4, 5, 6])
print(my_list3)

my_list4= [1, 2, 3]
# Prendre le contenu des autres conteneurs de données et l'ajoute à la fin de la liste
my_list4.extend([4, 5, 6])
print(my_list4)

my_list5 = [1, 2, 3]
# supprimer l'élément(index)
# my_list5.pop(0)
# supprimer la première correspondance d'un élément de la liste
# my_list5.remove(1)
# supprimer l'élément(index)
del my_list5[0]
print(my_list5)

my_list6 = [1, 2, 3, 2, 3]
# supprimer la première correspondance d'un élément de la liste
my_list6.remove(2)
print(my_list6)

my_list7 = [1, 2, 3]
# Effacer le contenu de la liste
my_list7.clear()
print(my_list7)

my_list8 = [1, 1, 1, 2, 3]
"""
a = 0
count = 0
while a < len(my_list8):
    if my_list8[a] == 1:
        count += 1  # count = count + 1
    a += 1
print(count)
"""
# Compter le nombre d'éléments dans une liste
print(my_list8.count(1))
# Compter le nombre d'éléments dans une liste
print(len(my_list8))
