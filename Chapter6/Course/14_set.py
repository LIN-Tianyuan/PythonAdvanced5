# Dénifition d'un set: Déduplication et non ordonnée
name = {"Python", "666", "Python", "y6"}
print(name)
# Longueur d'un set
print(len(name))
print("------------")
# Ajout d'un nouvel élément
my_set = {"Leo", "Laurent"}
my_set.add("Kevin")
print(my_set)
# Supprimer l'élément
my_set.remove("Leo")
print(my_set)
print("------------")
my_set2 = {"Leo", "Laurent", "Kevin"}
element = my_set2.pop()
print(f"Element supprimé: {element}")
print(my_set2)
my_set2.clear()
print(my_set2)
print("------------")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set3: {set3}")
print(f"set1: {set1}")
print(f"set2: {set2}")
print("------------")
set4 = {1, 2, 3}
set5 = {1, 5, 6}
set4.difference_update(set5)
print(f"set4: {set4}")
print(f"set5: {set5}")
print("------------")
set6 = {1, 2, 3}
set7 = {1, 5, 6}
set8 = set6.union(set7)
print(f"set8: {set8}")
print(f"set6: {set6}")
print(f"set7: {set7}")
# Afficher le nombre d'éléments dans le set
set9 = {1, 2, 3}
print(len(set9))
print("------------")
set10 = {1, 2, 3}
# Traverser le set
for i in set10:
    print(i)

