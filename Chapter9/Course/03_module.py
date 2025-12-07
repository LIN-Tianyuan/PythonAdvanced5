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
from time import *
print("Début")
sleep(1)
print("Fin")
"""

# Alias du module
import time as tt
tt.sleep(2)
print("hello")