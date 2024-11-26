############################################
############## les Fonctions ###############
############################################

# Principe et généralités :

"""
En programmation, les fonctions sont très utiles pour réaliser plusieurs fois la même opération au sein d'un programme. 
Elles rendent également le code plus lisible et plus clair en le fractionnant en blocs logiques.

Vous connaissez déjà certaines fonctions Python. 
Par exemple math.cos(angle) du module math renvoie le cosinus de la variable angle exprimé en radian. 
Vous connaissez aussi des fonctions internes à Python comme range() ou len(). 
Pour l'instant, une fonction est à vos yeux une sorte de « boîte noire » :

1 - À laquelle vous passez aucune, une ou plusieurs variable(s) entre parenthèses. 
    Ces variables sont appelées arguments. 
    Il peut s'agir de n'importe quel type d'objet Python.

2 - Qui effectue une action.

3 - Qui renvoie un objet Python ou rien du tout.
"""

"""
Par exemple, si vous appelez la fonction len() de la manière suivante :
len([0, 1, 2])
>>> 3

voici ce qu'il se passe :

1 - vous appelez len() en lui passant une liste en argument (ici la liste [0, 1, 2]) ;
2 - la fonction calcule la longueur de cette liste ;
3 - elle vous renvoie un entier égal à cette longueur.
"""

"""
Aux yeux du developpeur, 
    une fonction est une portion de code effectuant une suite d'instructions bien particulière. 
Mais avant de vous présenter la syntaxe et la manière de construire une fonction, 
    revenons une dernière fois sur cette notion de « boîte noire » :

Une fonction effectue une tâche. Pour cela, elle reçoit éventuellement des arguments et renvoie éventuellement quelque chose. 
L'algorithme utilisé au sein de la fonction n'intéresse pas directement l'utilisateur. 
Par exemple, il est inutile de savoir comment la fonction math.cos() calcule un cosinus. 
On a juste besoin de savoir qu'il faut lui passer en argument un angle en radian, 
    et qu'elle renvoie le cosinus de cet angle. Ce qui se passe à l'intérieur de la fonction ne regarde que le developpeur.

Chaque fonction effectue en général une tâche unique et précise. 
Si cela se complique, il est plus judicieux d'écrire plusieurs fonctions (qui peuvent éventuellement s'appeler les unes les autres). 
Cette modularité améliore la qualité générale et la lisibilité du code. 
Vous verrez qu'en Python, les fonctions présentent une grande flexibilité.
"""

# Définition :

"""
Pour définir une fonction, Python utilise le mot-clé "def". 
Si on souhaite que la fonction renvoie quelque chose, il faut utiliser le mot-clé "return". 

Par exemple :
"""

def carre(x):
    return x**2

print("1  : ", carre(2) )

"""
Notez que la syntaxe de def utilise les deux-points comme les boucles for et while ainsi que les tests if : 
    un bloc d'instructions est donc attendu. 

De même que pour les boucles et les tests, 
    l'indentation de ce bloc d'instructions (qu'on appelle le corps de la fonction) est obligatoire.

Dans l'exemple précédent, 
    nous avons passé un argument à la fonction carre(), 
    qui nous a retourné une valeur que nous avons immédiatement affichée à l'écran avec l'instruction print(). 
    
Que veut dire valeur renvoyée ? Et bien cela signifie que cette dernière est récupérable dans une variable :
"""

resultat = carre(3)
print("2  : ", resultat )

"""
Ici, le résultat renvoyé par la fonction est stocké dans la variable resultat. 
Notez qu'une fonction ne prend pas forcément un argument et ne renvoie pas forcément une valeur, 
    par exemple :
"""

def hello():
    print("3  : ", "bonjour")

hello()

# Passage d'arguments

"""
Le nombre d'arguments que l'on peut passer à une fonction est variable. 
Nous avons vu ci-dessus des fonctions auxquelles on passait zero ou un argument. 
Dans les chapitres précédents, 
    vous avez rencontré des fonctions internes à Python qui prenaient au moins deux arguments. 
Souvenez-vous par exemple de range(1, 10) ou encore range(1, 10, 2). 
Le nombre d'arguments est donc laissé libre à l'initiative du programmeur qui développe une nouvelle fonction.
"""

"""
Une particularité des fonctions en Python est que vous n'êtes pas obligé de préciser le type des arguments, 
    dès lors que les opérations que vous effectuez avec ces arguments sont valides. 
Python est en effet connu comme étant un langage au « typage dynamique », 
    c'est-à-dire qu'il reconnaît pour vous le type des variables au moment de l'exécution. Par exemple :
"""

def fois(x, y):             # Cette fonction prend 2 arguments
    return x*y              # Cette fonction retourne le produit des deux parametres

print("4  : ", fois(2, 3))  # Ici une simple multiplication d'entiers

                            # Ici une multiplication d'un entier et d'une chaine de caractères
print("5  : ", fois("to", 2))

                            # Ici une multiplication d'un entier et d'une liste
print("6  : ", fois([1,3], 2))

# Renvoi de résultats

"""
Un énorme avantage en Python est que les fonctions sont capables de renvoyer plusieurs objets à la fois, 
    comme dans cette fraction de code :
"""

def carre_cube(x):
        # On pourrait aussi l'écrire : return (x**2, x**3) c'est donc l'autre manière d'écrire les tuples.
    return x**2, x**3       

                            # Ici on remarque que cela va retourner (4, 8) c'est bien un tuple.
print("7  : ", carre_cube(2))

"""
En réalité Python ne renvoie qu'un seul objet, mais celui-ci peut être séquentiel, 
    c'est-à-dire contenir lui-même d'autres objets. Dans notre exemple, Python renvoie un objet de type tuple, type que nous avons vu dans le chapitre 8 Dictionnaires et tuples (souvenez-vous, il s'agit d'une sorte de liste avec des propriétés différentes). Notre fonction pourrait tout autant renvoyer une liste :
"""
