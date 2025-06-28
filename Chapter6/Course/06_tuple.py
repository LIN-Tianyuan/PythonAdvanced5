# Définir un tuple
t1 = (1, 2, 'hello')
# Récupération des données par indice(index)
print(t1[2])

t2 = (1, 2, 'hello', 3, 4, 'hello')
# Trouver la première correspondance pour un élément spécifique
print(t2.index('hello'))

t3 = (1, 2, 3)
# Compter le nombre d'éléments dans un tuple
print(len(t3))

# On ne peut pas modifier le contenu d'un tuple
"""
t4 = (1, 2, 3)
t4[0] = 5
# TypeError: 'tuple' object does not support item assignment
"""

t5 = (1, 2, ['Leo', 'Lucas'])
t5[2][0] = 'Kevin'
print(t5)