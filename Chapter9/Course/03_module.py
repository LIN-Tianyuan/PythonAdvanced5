"""
# import module name
import time

print("Début")
time.sleep(1)
print("Fin")
"""

"""
# from module name import function name
from time import sleep
print("Début")
sleep(1)
print("Fin")
"""

"""
# from module name import *
# *: Importation de toutes les méthodes(fonctions) du module time
from time import *
print("Début")
sleep(1)
print("Fin")
"""

# Alias du module
import time as tt
tt.sleep(2)
print("hello")

# Alias de la fonction
from time import sleep as sl
sl(2)
print("hello")