############################################
############# les Dictionnaires ############
############################################

# Définition et fonctionnement :

"""
Un dictionnaire contient une collection d'objets Python auxquels on accède à l'aide d'une clé de correspondance plutôt qu'un indice. 
Ainsi, il ne s'agit pas d'objets séquentiels comme les listes, 
    mais plutôt d'objets dits de correspondance (mapping objects en anglais) ou tableaux associatifs.
"""

# Ceci étant défini, comment fonctionnent-ils exactement ? Regardons un exemple :

ville = {}                  # On defini un dictionnaire vide

    # On remplit le dictionnaire avec plusieurs clés ("nom", "population", "superficie") auxquelles on affecte des valeurs ("valence", 64483, 36.7).
ville["nom"] = "lyon"   
ville["population"] = 1702921
ville["superficie"] = 47.87

                            # Retourne : {'nom': 'lyon', 'population': 1702921, 'superficie': 47.87}
print("3  : ", ville)

"""
Une fois le dictionnaire créé, on récupère la valeur associée à une clé donnée avec une syntaxe du type dictionnaire["clé"].
"""

                            # Retourne : 'lyon'
print("4  : ", ville["nom"])

# On peut aussi initialiser toutes les clés et les valeurs d'un dictionnaire en une seule opération :

ville = {"nom": "valence", "population": 64483, "superficie": 36.7}

# Mais rien ne nous empêche d'ajouter une clé et une valeur supplémentaire :

ville["nombreDeDidierBarcelo"] = 1
print("5  : ", ville)       # Retourne : {'nom': 'valence', 'population': 64483, 'superficie': 36.7, 'nombreDeDidierBarcelo': 1}

"""
Les humains retiennent mieux les noms que les chiffres. 

Ainsi, les dictionnaires se révèlent très pratiques lorsque vous devez manipuler des structures complexes à décrire
    et que les listes présentent leurs limites. 
L'usage des dictionnaires rend en général le code plus lisible. Par exemple, si nous souhaitions stocker les coordonnées (x, y, z)
    d'un point dans l'espace, nous pourrions utiliser coors = [0, 1, 2] pour la version liste
    et coors = {"x": 0, "y": 1, "z": 2} pour la version dictionnaire. 
    
Quelqu'un qui lit le code comprendra tout de suite que coors["z"] contient la coordonnée z, ce sera moins intuitif avec coors[2].
"""

# La Fonction len()

"""
Comme pour les listes, 
    l'instruction len() renvoie la longueur du dictionnaire, 
    sauf qu'ici il s'agit du nombre de couples clé / valeur. 
    
Voici un exemple d'utilisation :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}
                            # Retournera : 3
print("6  : ", len( ville ) )

# Itération sur les clés pour obtenir les valeurs : 

"""
Si on souhaite voir toutes les associations clés / valeurs, on peut itérer sur un dictionnaire de la manière suivante :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}
for key in ville:
    print("7  : ", key, ":", ville[key])

"""
retournera :

nom : reykjavik
population : 139875
superficie : 274.5
"""

# Les méthodes .keys() et .values() :

"""
Les méthodes .keys() et .values() renvoient, comme vous vous en doutez, les clés et les valeurs d'un dictionnaire :
"""
ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}

                            # Retourne : dict_keys(['poids', 'nom', 'taille'])
print("8  : ", ville.keys())
                            # Retourne : dict_values([70, 'singe', 1.75])
print("9  : ", ville.values())

"""
Les mentions dict_keys et dict_values indiquent que nous avons à faire à des objets un peu particuliers. 
Ils ne sont pas indexables (on ne peut pas retrouver un élément par indice, par exemple dico.keys()[0] renverra une erreur). 
Si besoin, nous pouvons les transformer en liste avec la fonction list() :
"""

ville = {"nom": "reykjavik", "population": 139875, "superficie": 274.5}

                            # Renvoi : ['reykjavik', 139875, 274.5]
print("10 : ", list(ville.values()))

"""
Toutefois, on peut itérer dessus dans une boucle for (on dit qu'ils sont itérables) :

for cle in animal2.keys():
    print(cle)

Retourne :

nom
poids
taille
"""

# La méthode .items() :
