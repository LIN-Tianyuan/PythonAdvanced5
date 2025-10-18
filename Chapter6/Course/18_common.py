my_list = [1, 2, 3]
my_tuple = (1, 2, 3, 4, 5)
my_str = "Python"

# Compter le nombre d'éléments dans un conteneur
print(len(my_list))
print(len(my_str))
print(len(my_tuple))
print('----------')
# Le plus grand élément d'un contenur
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print('----------')
# Le plus petit élément d'un contenur
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print('----------')

my_list2 = [58, 45, 32, 76, 19]
# Trier le conteneur donné
# petit -> grand
print(sorted(my_list2))
# grand -> petit
print(sorted(my_list2, reverse=True))

print('----------')

print('abc' > 'abd')
print('a' > 'A')
print('key2' > 'key1')

