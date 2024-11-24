############################################
############### les Boucles ################
############################################

# Les boucles for :

"""
En programmation, on est souvent amené à répéter plusieurs fois une instruction. 
Incontournables à tout langage de programmation, 
    les boucles vont nous aider à réaliser cette tâche répétitive de manière compacte et efficace.
"""

"""
Imaginez par exemple que vous souhaitiez afficher les éléments d'une liste les uns après les autres. 
Dans l'état actuel de vos connaissances, 
    il faudrait taper quelque chose du style :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
print("1-1  : ", animaux[0])
print("1-2  : ", animaux[1])
print("1-3  : ", animaux[2])
print("1-4  : ", animaux[3])

"""
Si votre liste ne contient que 4 éléments, 
    ceci est encore faisable mais imaginez qu'elle en contienne 100 voire 1 000 ! 
Pour remédier à cela, il faut utiliser les boucles . 

Regardez l'exemple suivant :
"""

animaux = ["girafe", "tigre", "singe", "souris"]
for animal in animaux:
    print("2    : ", animal)

"""
Commentons en détails ce qu'il s'est passé dans cet exemple :

La variable animal est appelée variable d'itération , 
    elle prend successivement les différentes valeurs de la liste animaux à chaque itérations (ou tour) de boucle.

On verra un peu plus loin dans ce chapitre que l'on peut choisir le nom que l'on veut pour cette variable. 
Celle-ci est créée par Python la première fois que la ligne contenant le for est exécutée (si elle existait déjà son contenu serait écrasé). 
Une fois la boucle terminée, 
    cette variable d'itération animal n'est pas détruite et conserve la dernière valeur de la liste animaux (ici la chaîne de caractères "souris").

Notez bien les types des variables utilisées ici :

animaux est une liste sur laquelle on itère ;
animal est une chaîne de caractères car chaque élément de la liste animaux est une chaîne de caractères.

Nous verrons plus loin que la variable d'itération peut être de n'importe quel type selon la liste parcourue.
En Python, une boucle itère la plupart du temps sur un objet dit séquentiel (c'est-à-dire un objet constitué d'autres objets) tel qu'une liste. 
De tels objets sont dits itérables car on peut effectuer une boucle dessus. 
Nous verrons aussi plus tard d'autres objets séquentiels sur lesquels on peut itérer dans une boucle.

D'ores et déjà, prêtez attention au caractère deux-points « : » à la fin de la ligne débutant par for. 
Cela signifie que la boucle for attend un bloc d'instructions, 
    en l’occurrence toutes les instructions que Python répétera à chaque itération de la boucle. 
    
On appelle ce bloc d'instructions le corps de la boucle. 

Comment indique-t-on à Python où ce bloc commence et se termine ? Cela est signalé uniquement par l'indentation,
    c'est-à-dire le décalage vers la droite de la (ou des) ligne(s) du bloc d'instructions.
"""
