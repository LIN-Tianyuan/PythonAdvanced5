# Paramètres formelles
def user_info(name, age, gender):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")

# 1. arguments positionnels
# Paramètres réelles
user_info("Alex", 18, "homme")
# 2. arguments mots-clés
user_info(name="Alex", age=18, gender="homme")
# Peut ne pas suivre un ordre fixe
user_info(age=18, name="Alex", gender="homme")
# Peut être mélangé avec les arguments potisionnels
user_info("Alex", gender="homme", age=18)

# 3. arguments par défaut
def user_info2(age, gender, name="Alex"):
    print(f"Votre nom est {name}, votre âge est {age} ans et votre sexe est {gender}.")

user_info2(18, "homme")
user_info2(18, "femme", "Lucie")

# 4. Arguments de longueur indéterminée
# 4.1 Passage de argument positionnels
def user_info3(*args):
    print(args)

user_info3("Alex")
user_info3("Luna", 18)

# 4.2 Passage de argument mot-clé
def user_info4(**kwargs):
    print(kwargs)

user_info4(name="Alex", age=18, gender="homme")

