# Python

## Chapter 1 Introduction

- Naissance: 1991
- Un langage de programmation
- Pycharm: IDE(Integrated development environnement)

```python
print("Hello World!")
```

## Chapter 2 Syntaxe de base de Python

### 1. Littéral

- Littéral: Une valeur fixe qui est écrite dans le code.
- Type communs de littéral: int, float, string
- print(littéral)
  - print(10)
  - print(13.14)
  - print('python')

### 2. Commentaire

- Une déclaration explicative dans le code qui est utilisée pour annoter le contenu du code.
- Une seule ligne: # commentaire
- Multilignes: """commentaire contenu"""

### 3. Variable

- Une variable est utilisé pour enregistrer des données lors de l'exécution d'un programme.
- Format de la définition d'une variable:
  - Nom de la variable = Valeur de la variable
  - Example: name = "alex"
- La valeur d'une variable peut être modifiée.

```bash
+ - * / // % **
```

- type() peut être utilisée pour voir le type des données.
- Les variables n'ont pas de type, mais les données qu'elles stockent en ont un.

- Converision des données:
  - int(x)
  - float(x)
  - str(x)
- Tout type peut être converti en chaîne de caractères.

- La chaîne de caractères doit réellement être un nombre à l'intérieur pour convertir la chaîne de caractères en un nombre.

```python
int_num = int(11.345)
print(int_num) # 11
```

- Identifiant: Les noms que les utilisateurs écrivent pour les variables, les classes ,les méthodes, etc.
- Règles:
  - Qualifié par le contenu
  - Sensible à la casse
  - Pas de mots-clés
- Convention:
  - Voir le nom pour connaître la signification
  - Nomenclature des tirets bas
  - Toutes les lettres minuscules de l'alphabet

### 4. Opérateur

- Opérateurs arithmétiques:

```bash
+ - * / // % **
```

- Opérateurs d'affectation:
  - Affectation standard: =
  - Affectation composite: +=, -=, *=, /=, //=, %=, **=
  - c += a est équivalent à c = c + a

```python
a = 10
a = a + 10 # a += 10
print(a) # 20
```

### 5. Expansion de la chaîne de caractères

- Définition:

```bash
'alex'  "alex"  """alex"""
```

- Vous pouvez écrire des guillemets doubles à l'intérieur de guillemets simple ou des guillemets simples à l'intérieur de guillemets doubles.
- "+" pour concaténer des variables ou des chaînes littérales.

### 6. Formatage des chaînes de caractères

```python
name = 'Alex'
age = 18
print("Je m'appelle %s et j'ai %d ans." % (name, age))
```

- String: %s
- Int: %d
- Float: %f

- Contrôle de précision:
  - Contrôles de la forme m.n, par exemple %5d, %5.2f, %.2f
  - .n arrondit les parties décimales.

```python
number1 = 50
number2 = 50.897
print("Digital 50 limite de largeur 5: %5d" % number1)
print("Digital 50 limite de largeur 1: %1d" % number1)
print("Chiffre 50.897 limite de largeur 7, précision décimale 2: %7.2f" % number2)
print("Chiffre 50.897 largeur illimitée, précision décimale 2: %.2f" % number2)

"""
Digital 50 limite de largeur 5:    50
Digital 50 limite de largeur 1: 50
Chiffre 50.897 limite de largeur 7, précision décimale 2:   50.90
Chiffre 50.897 largeur illimitée, précision décimale 2: 50.90
"""
```

### 7. Formatage des chaînes de caractères 2

- f"{variable} {variable}" pour un formatage rapide.

```python
name = 'Alex'
age = 18
height = 1.83
print(f"Je m'appelle {name} et j'ai {age} ans et je mesure {height} m.")
```

### 8. Formatage des expression

- Une expression est une instruction de code avec un résultat explicite.

```python
# Formatage des expression
print("Le résultat de 1 * 1 est: %d" % (1 * 1))
print(f"Le résultat de 1 * 1 est: {1 * 1}")
print("Le type de chaîne de Python est: %s" %type('chaîne'))
```

### 9. Saisie de données

- input(): récupérer les données saisie par le clavier.
- Les données obtenues seront toujours de type str.

## Chapter 3 Déclarations de jugement

### 1. Type booléen et opérateur de comparaison

- Type booléen: True / False
- Opérateur de comparaison:
  - == != > < >= <=

### 2. Format de base des instructions if else

```python
print("Bienvenue au parc d'attractions!")
# Obtenir l'entrée du clavier
age = int(input("Veuillez entrer votre âge: "))

# Déterminer si une personne est un adulte
if age >= 18:
    print("Vous êtes un adulte et devez acheter un billet pour la visite, 10euro.")
else:
    print("Vous êtes mineur et pouvez jouer gratuitement!")

print("Bonne visite!")
```

### 3. Format de base des instrctions if elif else

```python
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
```

### 4. Jugement impliquées

- Les déclarations de jugement imbriquées peuvent être utilisées pour des jugements logiques multi-conditionnels et multi-niveaux.

```python
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
```

## Chapter 4 Boucles

### 1. While

```python
a = 0
while a < 100:
    print("Xiao Mei, I love you.")
    a = a + 1
```

```python
# Boucles imbriquées
i = 1
while i <= 100:
    print(f"Today is day {i}, Ready to confess my love...")
    j = 1
    while j <= 10:
        print(f"Number of roses sent to Xiao Mei: {j}")
        j = j + 1
    print("Xiao Mei, I love you.")
    i = i + 1

print(f"Persistence to the number of days: {i - 1}, show love successfully!")
```

### 2. For

```python
name = "Python"
for letter in name:
    print(letter)
```

### 3. range

- range: obtenir une séquence de nombres (un des types itérables)

```python
for element in range(5):
    print(element)
```

- range(5): 0 1 2 3 4
- range(1, 5): 1 2 3 4
- range(5, 10 ,2): 5 7 9

### 4. break

- Terminer directement la boucle dans laquelle il se trouve

### 5. continue

- Interrompre l'exécution actuelle de la boucle dans laquelle vous vous trouvez et passer directement à la suivante.

## Chapter 5 Fonction

### 1. Introduction

- Des segments de code organisés et réutilisables
- Utilisés pour réaliser des fonctions spécifiques

### 2. Définition des fonctions

```bash
def nom de la fonction(paramètre entrant):
		fonction corps
		return la valeur de retour
```

- Définir d'abord la fonction et après appeler la fonction.

### 3. Paramètres entrants

- Accepter les données entrantes externes pendant que la fonction est en cours d'exécution.

```python
def add(x, y):
    print(x + y)
```

- Les paramètres de la définition de la fonction sont appelés paramètres formels.
- Les paramètres dans les appels de fonction sont appelés paramètres réels.

### 4. Valeur de retour

- Le résultat renvoyé à l'appelant après la fin de l'exécution de la fonction.
- Le mot-clé: return
- Le corps de la fonction se termine lorsqu'il rencontre return, donc le code écrit après return n'est pas exécuté.

```python
def add(x, y):
    return x + y

num = add(1, 2)
print(num)
```

### 5. None

- None est un littéral du type 'NoneType' et est utlisé pour indiquer: vide, sans signification
- Scénarios d'utilisation:
  - valeur de retour des fonctions
  - if le jugement
  - définition de la variable

```python
def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None

result = check_age(5)
if not result:
    print("No enter!")
```

### 6. Document de description des fonctions

- explication de la fonction pour aider à mieux comprendre sa fonction.
- param est utilisé pour interpréter les paramètres.
- return est utlisé pour interpréter la valeurs de retour.

```python
def add(x, y):
    """
    Additioner les deux chiffres
    :param x: Chiffre1
    :param y: Chiffre2
    :return: La somme
    """
    return x + y
```

### 7. Global

- Variable locale: Peut être utilisé à l'intérieur de la fonction et ne peut être utilisé en dehors de celle-ci.
- Variable globale: Peut être utilisé à l'intérieur comme à l'extérieur.
- Utiliser le mot-clé **global** pour déclarer une variable définie dans une fonction comme une variable globale.

## Chapter 6 Conteneur de données

### 1. list

```python
name_list = ['Leo', 'Lucas', 'Laurent']
# Trouver l'indice(index) d'un élément
print(name_list.index("Laurent"))
# Insertion d'un élément
name_list.insert(1, 'Kevin')
print(name_list)
print("-----------")

my_list = [1, 2, 3]
# Modifier la valeur d'un élément à une position spécifique(index)
my_list[0] = 5
print(my_list)

my_list2 = [1, 2, 3]
# Ajouter un élément
my_list2.append(4)
print(my_list2)

my_list3= [1, 2, 3]
my_list3.append([4, 5, 6])
print(my_list3)

my_list4= [1, 2, 3]
# Prendre le contenu des autres conteneurs de données et l'ajoute à la fin de la liste
my_list4.extend([4, 5, 6])
print(my_list4)

my_list5 = [1, 2, 3]
# supprimer l'élément(index)
# my_list5.pop(0)
# supprimer la première correspondance d'un élément de la liste
# my_list5.remove(1)
# supprimer l'élément(index)
del my_list5[0]
print(my_list5)

my_list6 = [1, 2, 3, 2, 3]
# supprimer la première correspondance d'un élément de la liste
my_list6.remove(2)
print(my_list6)

my_list7 = [1, 2, 3]
# Effacer le contenu de la liste
my_list7.clear()
print(my_list7)

my_list8 = [1, 1, 1, 2, 3]
"""
a = 0
count = 0
while a < len(my_list8):
    if my_list8[a] == 1:
        count += 1  # count = count + 1
    a += 1
print(count)
"""
# Compter le nombre d'éléments dans une liste
print(my_list8.count(1))
# Compter le nombre d'éléments dans une liste
print(len(my_list8))
```

- Chaque élément d'une liste a un nombre appelé indice(index).
- List[index] pour récupérer l'élément d'une liste.
- Caractéristiques:
  - contenir plusieurs éléments
  - contenir des éléments de différents types
  - **les données sont stockées de manière ordonnée (index)** 
  - l'existencede données en double est autorisée
  - peut être modifié(ajout ou suppression)

