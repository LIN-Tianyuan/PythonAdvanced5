# Définition d'une dictionnaire
stu_score = {
    "Léon": 99,
    "Lucy": 88,
    "Alex": 77
}
# Accès aux données du dictionnaire
print(stu_score["Léon"])
print(stu_score["Alex"])

# Dictionnaire imbriqué
stu_score2 = {
    "Tom": {
        "Math": 77,
        "English": 66,
        "Chinese": 55
    },
    "Lucy": {
        "Math": 64,
        "English": 90,
        "Chinese": 98
    },
    "Luna": {
        "Math": 79,
        "English": 45,
        "Chinese": 23
    }
}

print(stu_score2["Lucy"]["English"])

stu_score3 = {
    "Léon": 99,
    "Lucy": 88,
    "Alex": 77
}

# Modifier l'élément
stu_score3["Lucy"] = 90
print(stu_score3)

# Ajouter un élément
stu_score3["Luna"] = 66
print(stu_score3)

# Supprimer un élément
score_luna = stu_score3.pop("Luna")
print(score_luna)
print(stu_score3)

stu_score3.clear()
print(stu_score3)

stu_score4 = {
    "Léon": 99,
    "Lucy": 88,
    "Alex": 77
}

# Obtenir toutes les clés
keys = stu_score4.keys()
print(keys)

for key in keys:
    print(key)

# Objenir toutles les valeurs
values = stu_score4.values()
for value in values:
    print(value)

print("----------")
# Itération de dictionnaire
stu_score5 = {
    "Léon": 99,
    "Lucy": 88,
    "Alex": 77
}

keys = stu_score5.keys()
for key in keys:
    print(f"{key} {stu_score5[key]}")

print("----------")
# Calculer le nombre de tous les éléments
print(len(stu_score5))
