############################################
################ les Listes ################
############################################

"""
Les listes (ou list / array ) en python sont une variable dans laquelle on peut mettre plusieurs objets.

pour definir une liste il y a plusieurs moyen :
"""

# definition directe :

liste = []                  # defini une liste vide, sans elements de longueur 0

liste = [1, 2, 3, 4, 5]     # defini une liste de Ints de longueur 5, elle contien : 1, 2, 3 ... 5

                            # defini une liste de Strings de longueur 5, elle contien :  "1", "a" ... "True"
liste = ["1", "a", "Mattéo", "Python", "True"]   

                            # Une liste peut contenir plusieurs types d'objets differents :
                            # même des listes, on peut donc avoirs des listes dans des listes dans des listes ... etc   
liste = [1, "a", [], "Python", True]

# definition par la fonction list() :

liste = list("abcdef")
print("1  : ", liste)       # va retourner : ['a', 'b', 'c', 'd', 'e', 'f'], moins pratique mais plus rapide

# Utilisation : 

"""
Un des gros avantages d'une liste est que vous accédez à ses éléments par leur position. Ce numéro est appelé indice (ou index) de la liste.

liste  : ["girafe", "tigre", "singe", "souris"]
indice :        0        1        2         

Soyez très attentif au fait que les indices d'une liste de n éléments commencent à 
0 et se terminent à n-1 .
"""

    # Acceder à un element :
liste = [0, 1, 2, 3, 4, 5]
elementN0 = liste[0]        # nom_de_la_liste [indice de l'element]
print("2  : ", elementN0)   # retourne 0

    # En revanche liste [6] va retourner l'erreur : IndexError: list index out of range, car l'element n°6 n'existe pas

# Opération sur les listes

    # Tout comme les chaînes de caractères, les listes supportent l'opérateur + de concaténation, ainsi que l'opérateur * pour la duplication :

liste1 = ["girafe", "tigre"]
liste2 = ["singe", "souris"]

liste1 + liste2             # Retourne : ['girafe', 'tigre', 'singe', 'souris']

liste1 * 3                  # Retourne : ['girafe', 'tigre', 'girafe', 'tigre', 'girafe', 'tigre']

    # Ajouter un element a une liste : 

liste = []                  # Une liste vide

liste1 = liste + [15]       # Ou liste += [15] 
print("3  : ", liste)       # retournera : [15] 
liste = liste + [-5]        # Ou liste += [-5] 
print("4  : ", liste)       #retournera : [15, -5]

# Puis avec la méthode .append() :

liste = []
liste.append(15)            # retournera : [15] 

"""
Indiçage négatif :
Une liste peut également être indexée avec des nombres négatifs selon le modèle suivant :

liste          : ["girafe", "tigre", "singe", "souris"]
indice positif :        0        1        2         3
indice négatif :       -4       -3       -2        -1

ou encore :

liste          : ["A", "B", "C", "D", "E", "F"]
indice positif :   0    1    2    3    4    5
indice négatif :  -6   -5   -4   -3   -2   -1

Les indices négatifs reviennent à compter à partir de la fin. 
Leur principal avantage est que vous pouvez accéder au dernier élément d'une liste à l'aide de l'indice -1
    sans pour autant connaître la longueur de cette liste. 
L'avant-dernier élément a lui l'indice -2, l'avant-avant dernier l'indice -3, etc.
"""

# Les Tranches

"""
Un autre avantage des listes,
    est la possibilité de sélectionner une partie d'une liste en utilisant un indiçage construit sur le modèle :
        
        tranche = nomDeLaListe[ m : n+1 ]

        ici, on a récupéré tous les éléments du émième au énième (de l'élément m inclu à l'élément n+1 exclu) grace au ":"
    
    On dit alors qu'on récupère une tranche de la liste.
"""

                            # Defini une liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0ème au 2ème exclu donc [0, 1]
print("5  : ", listeDeNombres[0:2])  

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0ème au 3ème exclu donc [0, 1, 2]
print("6  : ", listeDeNombres[0:3])  

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 3ème jusqu'à la fin de la liste donc [3, 4, 5]
print("7  : ", listeDeNombres[3:]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste donc [0, 1, 2, 3, 4, 5]
print("8  : ", listeDeNombres[:]) 

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres : [1, 2, 3, 4]
print("9  : ", listeDeNombres[1:-1]) 

"""
On peut aussi préciser le pas en ajoutant un symbole deux-points supplémentaire et en indiquant le pas par un entier
"""

                            # Defini une liste de Ints de longueur 6, elle contien : 1, 2, 3 ... 5
listeDeNombres = [0, 1, 2, 3, 4, 5]

                            # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 0ème au 3ème exclu de 2 en 2 donc [0, 2]
print("10 : ", listeDeNombres[0:3:2]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste de 1 en 1 donc [0, 1, 2, 3, 4, 5]
print("11 : ", listeDeNombres[::1]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du début jusqu'à la fin de la liste de 2 en 2 donc [0, 2, 4,]
print("12 : ", listeDeNombres[::2]) 

    # Va retourner une nouvelle liste contenant des elements de listeDeNombres du 1er au 6ème exclu de 3 en 3 donc [1, 4]
print("13 : ", listeDeNombres[1:6:3]) 
