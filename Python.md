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

### 2. Format de base des instructions if



