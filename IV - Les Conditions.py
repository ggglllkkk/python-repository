############################################
############# les Conditions ###############
############################################

"""
Les tests sont un élément essentiel à tout langage informatique si on veut lui donner un peu de complexité
    car ils permettent à l'ordinateur de prendre des décisions. 

Pour cela, Python utilise le mot clé if ainsi qu'un boolean que nous avons abordée plus tôt
"""

x = int( 2 )
condition = x == 2

if condition:
    print("1  : ", "Le test est vrai !")

    # On peut l'écrire plus simplement :

x = int( 2 )

if x == 2:
    print("2  : ", "Le test est vrai !")

    # La condition peut aussi être plus complexe :

x = int( 2 )
y = int( 6 )
z = bool( True )

    # On peut traduire par : si ((x egal 2 et x (superieur ou egal à 2)) et le reste de la division euclidienne de y par 2 egal 0) ou z est vrai
if ((x == 2 and x >= 2 ) and y % 2 == 0) or z:
    print("3  : ", "Le test est vrai !")

    # Si la condition testée est fausse on peut definir une action à faire par defaut :

x = int( 3 )

if x == 2:
    print("4  : ", "Le test est vrai !")
else:
    print("4  : ", "Le test est faux !")

    # On peut echainer les tests de conditions :

x = int( 4 )

if x == 2:
    print("5  : ", "x = 2")
else: 
    if x == 3:
        print("5  : ", "x = 3")
    else :
        print("5  : ", "x est different de 2 et 3")

    # On peut l'écrire plus simplement :

x = int( 4 )

if x == 2:
    print("6  : ", "x = 2")
elif x == 3:                # On peut rajouter autant de elif à la suite que l'on souhaite
    print("6  : ", "x = 3")
else:                       # Mais uniquement un seul else      
    print("6  : ", "x est different de 2 et 3")

"""
ATTENTION :

if :
    ...
if :
    ...
if :
    ...

N'est pas similaire à :

if :
    ...
elif :
    ...
elif :
    ...

Dans le premier cas, toutes les conditions seront testée, 
    c'est à dire que si la première condition est verifiée et que le code associé est éxécuté,
    la deuxième condition peut être verifiée et éxécutée,
    etc ...

Dans le deuxième cas, toutes les conditions peuvent être testées mais pas forcément,
    c'est à dire que si la première condition est verifiée et que le code associé est éxécuté,
    le script va sauter toutes les autres conditions et va poursuivre l'éxécution du script.
"""
