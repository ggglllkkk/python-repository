"""
En programmation on peut se retrouver confrontés à une situation où il nous est nécessaire de trier (par ordre croissant) les éléments d'une liste.
Nous allons voir les 3 types de tri les plus utilisés, à savoir le tri par insertion, le tri par sélection et le tri par bulles.
Cependant, il arrive d'avoir des liste ne contenant pas QUE des nombres à trier, nous verrons donc à la fin comment élargir les possibilités de tri.

Pour commencer, il est recommandé d'utiliser la fonction par défaut de python, sorted, dû à son coût machine des plus optimisés.

"""

listeATrier = [0, 89 , -7 , 18 , 52 , 3]
listeTriee = sorted(listeATrier)   # La méthode sorted() va retourner la liste qui lui est passée en argument triée par ordre croissant
print("1: ", listeTriee)     


listeATrier = [0, 89 , -7 , 18 , 52 , 3]
listeTriee = sorted(listeATrier, reverse=True)   # L'argument reverse détermine l'ordre de tri. Il est par défaut égal à False (=croissant), en le passant à True l'ordre devient décroissant
print("2: ", listeTriee)   


"""
Nous allons maintenant voir comment fonctionne le tri par insertion.

Principe général:

On considère notre liste à trier 'séparée' en deux parties, une triée et une non triée.
Par défaut, la liste triée correspond au premier élément, on a donc :

[0 , 89 , -7 , 18 , 52 , 3]
trié|         pas trié

Pour chaque élément non trié en partant de la gauche, on va le permuter avec le nombre le précédant tant que ce dernier n'est pas plus petit que celui sélectionné (ou qu'on atteigne le début de la liste).
Ainsi on aura:

[0 , 89 , -7 , 18 , 52 , 3]     etat initial
trié|        pas trié


On sélectionne 89.

0<89 donc on s'arrete la. On a donc:
[0 , 89 , -7 , 18 , 52 , 3]
trié   |       pas trié


On sélectionne -7.

89>-7 donc on les permute. On a donc:
[0, -7 , 89 , 18 , 52 , 3]

0>-7 donc on les permute. On a donc:
[-7 , 0 , 89 , 18 , 52 , 3]

-7 est en index 0 donc on s'arrete la. On a donc:
[-7 , 0 , 89 , 18 , 52 , 3]
trié       |  pas trié


On sélectionne 18.

89>18 donc on les permute. On a donc:
[-7 , 0 , 18 , 89 , 52 , 3]

0<18 donc on s'arrete la. On a donc:
[-7 , 0 , 18 , 89 , 52 , 3]
trié              | pas trié

Et on continue ainsi jusqu'atteindre la fin de la liste.

En code, ça donne ceci:
"""

liste=[0, 89 , -7 , 18 , 52 , 3]

for k in range(1, len(liste)):                         # boucle dans la liste (et commence à 1!)
    i=k                                                # i sera la variable déterminant l'index actuel de l'élément sélectionné
    while i!=0 and liste[i] < liste[i-1]:              # littéralement: TANT QU'on est pas au début de la liste ET que l'élément sélectionné plus petit que son prédécesseur
        liste[i], liste[i-1] = liste[i-1], liste[i]    # on inverse l'élément sélectionné et son prédécesseur
        i-=1                                           # on décale d'un cran vers la gauche

print("3: ", liste)

"""
Il suffit d'inverser le sens du comparateur pour inverser le sens de tri.

!!!!!!! Dans la condition du WHILE, il faut ECRIRE LE i!=0 EN PREMIER
En effet, sinon, on cherche un index négatif qui n'existera pas (en python si mais on ne le veut pas)
Par principe de fainéantise, si la première des deux clauses d'un AND est fausse, python ne lira pas la deuxième, évitant ainsi de potentielles erreurs d'index.
"""
