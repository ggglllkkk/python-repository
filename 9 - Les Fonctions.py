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
