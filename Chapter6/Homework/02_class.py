import random
profs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
classes = [[], [], []]

for prof in profs:
    number = random.randint(0, 2)
    classes[number].append(prof)

print(classes)


