############################################
############# les Boucles While ############
############################################

"""
Une alternative à l'instruction for couramment utilisée en informatique est la boucle while. 
Avec ce type de boucle, 
    une série d'instructions est exécutée tant qu'une condition est vraie. 
"""

# Par exemple :

i = 1
while i <= 4:
    print("1  : ", i)
    i = i + 1

"""
Remarquez qu'il est encore une fois nécessaire d'indenter le bloc d'instructions correspondant au corps de la boucle (ici, les instructions lignes 3 et 4).

Une boucle while nécessite généralement trois éléments pour fonctionner correctement :

>>> Initialisation de la variable d'itération avant la boucle (ligne 1).

>>> Test de la variable d'itération associée à l'instruction while (ligne 2).

>>> Mise à jour de la variable d'itération dans le corps de la boucle (ligne 4).

Faites bien attention aux tests et à l'incrémentation que vous utilisez, 
    car une erreur mène souvent à des « boucles infinies » qui ne s'arrêtent jamais. 
Vous pouvez néanmoins toujours stopper l'exécution d'un script Python à l'aide de la combinaison de touches Ctrl-C
    (c'est-à-dire en pressant simultanément les touches Ctrl et C).
"""
