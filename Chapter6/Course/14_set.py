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