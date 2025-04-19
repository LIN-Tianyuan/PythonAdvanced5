import random
number = random.randint(1, 100)
print(number)
player = int(input("Veuillez deviner un numéro: "))
if number == player:
    print("Félicitation, vous avez réussi du premier coup!")
else:
    player = int(input("Mauvaise réponse, encore une fois: "))
    if player == number:
        print("Félicitations pour votre bonne réponse!")
    else:
        player = int(input("Mauvaise réponse, encore une fois: "))
        if player == number:
            print("Félicitations pour votre bonne réponse!")
        else:
            print("Désolé, vous avez mal deviné.")