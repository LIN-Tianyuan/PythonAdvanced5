# Si un fichier de module possède une variable __all__, 
# lorsqu'il est importé en utilisant from xxx import *,
# seul les éléments de cette liste peuvent être importés.
# __all__ = ['test_a']

def test(a, b):
    print(a + b)

def test_a():
    print("testA")

def test_b():
    print("testB")

# Appeler la fonction uniquement dans le fichier actuel, si la condition n'est pas remplie dans les autres fichiers
# importés, l'appel de la fonction de test ne sera pas exécuté.
if __name__ == "__main__":
    test(1, 1)

# def test_a():
#     print("testA")
#
# def test_b():
#     print("testB")
#
# if __name__ == "__main__":
#     test(1, 3)