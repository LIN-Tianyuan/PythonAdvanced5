"""
try:
    f = open("linux.txt", "r")
    print(f.readlines())
    f.close()
except:
    f = open("linux.txt", "w")
    f.close()
"""

"""
name = "Alex"
try:
    print(name)
except NameError as e:
    print("Erreur de nom de variable non définie.")
"""

"""
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print("Erreur de ZéroDivision")
"""

"""
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)
"""

"""
try:
    # print(1)
    print(num)
except Exception as e:
    print(e)
# else indique le code à exécuter s'il n'y pas d'exception
else:
    print("Je suis else, le code qui est exécuté quand il n'y pas d'exception.")
"""

try:
    f = open("text.txt", "r")
except Exception as e:
    f = open("text.txt", "w")
else:
    print("Aucune anomalie, donc heureux.")
# finally indique le code qui doit être exécuté sans tenir compte des exceptions,
# par exemple la fermeture d'un fichier
finally:
    f.close()





