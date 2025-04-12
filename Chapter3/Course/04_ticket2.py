print("Bienvenue au Zoo!")
height = int(input("Veuillez indiquer votre taille(cm): "))
vip_level = int(input("Veuillez entrer votre niveau VIP(1~5): "))
day = int(input("Veillez entrer la date du jour (1~30): "))
if height < 120:
    print("Vous pouvez jouer gratuitement si vous mesurez moins de 120 cm.")
elif vip_level > 3:
    print("Votre niveau vip est supérieur à 3 et vous pouvez jouer gratuitement.")
elif day == 1:
    print("Aujourd'hui est le 1er jour libre pour visiter.")
else:
    print("Désolé, toutes les conditions ne sont pas remplis et un billet est nécessaire pour 10 euro.")

print("Bonne visite!")