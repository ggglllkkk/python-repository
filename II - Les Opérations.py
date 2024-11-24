############################################
############# les Opperations ##############
############################################

# voici tout les opperateurs : + * - / // % **

# L'addition : 

a = int( 1 ) 
b = int( 2 )
resultat = a + b 
print(resultat)             # egale à 3 un int

a = float( 1.0 ) 
b = int( 2 )
resultat = a + b 
print(resultat)             # egale à 3.O un Float

"""Astuce"""
# Au lieu d'ecrire :
a = a + 3                   # Pour que la valeur de a augmente de 3
# On peut ecrire
a += 3

# L'addition entre un str et un int est impossible

# L'addition entre un str et un float est impossible

a = str( "a") 
b = str( "2" )
resultat = a + b 
print(resultat)             # egale à "a2" un Str

a = str( "1") 
b = str( "2" )
resultat = a + b 
print(resultat)             # pas egale à "3" un Str, ni à 3 un int, mais bien à "12" la reunion des deux chaines de caractère

a = str( "Je m'appelle ") 
b = str( "Mattéo" )
resultat = a + b 
print(resultat)             # renvoie "Je m'appelle Mattéo" un Str

a = bool( 1 ) 
b = bool( 1 )
resultat = a + b 
print(resultat)             # egale à 2, laddition transforme les bool en Int, l'addition de deux Bool c'est le mot clé "and"

# La soustraction : 

a = int( 1 ) 
b = int( 2 )
resultat = a - b 
print(resultat)             # egale à -1

# La soustraction entre un str et un int est impossible

# La soustraction entre un str et un float est impossible

# La soustraction entre un str et un str est impossible

# La multiplication :

a = int( 2 ) 
b = int( 3 )
resultat = a * b 
print(resultat)             # egale à 6 un int

a = float( 3.0 ) 
b = int( 2 )
resultat = a * b 
print(resultat)             # egale à 6.O un Float

"""Astuce"""
# Au lieu d'ecrire :
a = a * 3                   # Pour que la valeur de a soit multipliée par 3
# On peut ecrire
a *= 3

a = str( "a" ) 
b = int( 4 )
resultat = a * b 
print(resultat)             # egale à "aaaa" un str

# La multiplication entre un str et un float est impossible

# La multiplication entre un str et un str est impossible

a = bool( True ) 
b = int( 4 )
resultat = a * b 
print(resultat)             # retourne 4 si a = True, sinon 0

# Avec la multiplication, les bool peuvent servir d'indicatrice

x = int( -2 )
isPositive = x > 0
isNegativeOrNull = not isPositive
                            # retourne 8 si (x > 0) et 5 sinon
print(8*isPositive + 5*isNegativeOrNull)
                            # peut aussi s'ecrire plus rapidement : (plus compacte mais moins lisible)
print(8*(x > 0) + 5*(not x > 0))

# La division :

a = int( 1 ) 
b = int( 2 )
resultat = a / b 
print(resultat)             # egale à 0.5 un Float, la division retournera toujours un Float

"""Astuce"""
# Au lieu d'ecrire :
a = a / 3                   # Pour que la valeur de a soit divisée par 3
# On peut ecrire
a /= 3

    # la division ne fonctionne qu'avec des Int et des Floats

# La division entière : //

# le mot clé // permet d'obtenir le resultat de la division eclidienne sans le reste

a = int( 5 ) 
b = int( 2 )
resultat = a // b 
print(resultat)             # egale à 2, car 5 = 2 * 2 + 1, // renverra un Int

a = float( 5.0 ) 
b = float( 2.0 )
resultat = a // b 
print(resultat)             # egale à 2.0, car 5.0 = 2.0 * 2.0 + 1.0, // renverra un Float

    # la division entière ne fonctionne qu'avec des Int et des Floats

# Le reste de la division euclidienne (modulo) : %

# le mot clé % permet d'obtenir le reste de la division eclidienne.

a = int( 5 ) 
b = int( 2 )
resultat = a % b 
print(resultat)             # egale à 1, car 5 = 2 * 2 + 1, // renverra un Int

a = float( 5.0 ) 
b = float( 2.0 )
resultat = a % b 
print(resultat)             # egale à 1.0, car 5.0 = 2.0 * 2.0 + 1.0, // renverra un Float

    # le reste de la division euclidienne ne fonctionne qu'avec des Int et des Floats

# La puissance : **

a = int( 5 ) 
b = int( 2 )
resultat = a ** b 
print(resultat)             # egale à 25, car 5 puissance 2 = 25, ** renverra un Int

a = float( 5.0 ) 
b = float( 2.0 )
resultat = a ** b 
print(resultat)             # egale à 25.0, car 5.0 puissance 2.0 = 25.0, ** renverra un Float

    # le reste de la division euclidienne ne fonctionne qu'avec des Int et des Floats
