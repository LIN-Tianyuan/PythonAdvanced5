name = "Alex"
print(name[0])
print(name[-1])
"""
name[0] = 'a'
# TypeError: 'str' object does not support item assignment
print(name)
"""

name_string = "Leo and Laurent"
# Trouver la valeur de l'indice d'une chaîne spécifique
print(name_string.index('L'))       # 0
print(name_string.index('and'))     # 4

name_string2 = "Leo and Laurent"
# Remplacer str1 par str2
new_name_string2 = name_string2.replace('Leo', 'Kevin')
print(name_string2)
print(new_name_string2)

name_string3 = "Leo and Laurent"
# Diviser la chaîne de caractères en plusieurs selon la séparateur
name_list = name_string3.split(" ")
print(name_list)

name_string4 = "  Leo and Laurent  "
# Suppression des espaces avant et arrière
new_name_string4 = name_string4.strip()
print(new_name_string4)

name_string5 = "12Leo and Laurent21"
# Suppression de la châine spécifiée avant et arrière
new_name_string5 = name_string5.strip('12')
print(new_name_string5)

name_string6 = "Jean-Lucas and Lucas"
# Compter le nombre d'occurrences d'une chaîne de caractères
count = name_string6.count('Lucas')
print(count)
# Compter la longueur des châines de caractères
print(len(name_string6))
