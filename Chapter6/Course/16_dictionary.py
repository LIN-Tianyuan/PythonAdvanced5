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

stu_score3["Lucy"] = 90
print(stu_score3)




