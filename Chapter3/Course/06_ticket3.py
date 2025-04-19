print("Bienvenue au Zoo!")
height = int(input("Veuillez indiquer votre taille(cm): "))
vip_level = int(input("Veuillez entrer votre niveau VIP(1~5): "))
day = int(input("Veillez entrer la date du jour (1~30): "))
label = False
if height < 120:
    if vip_level > 3:
        if day == 1:
            print("Vous pouvez jouer gratuitement.")
            label = True
if not label:
    print("Désolé, toutes les conditions ne sont pas remplis et un billet est nécessaire pour 10 euro.")

print("Bonne visite!")