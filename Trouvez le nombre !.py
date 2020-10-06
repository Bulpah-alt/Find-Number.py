#Si mes explications dépassent, naviguez dans le code avec les flèches de l'ordinateur. Je tiens aussi à rappeler qu'elles sont facultatives. Elles vous permettent de comprendre le code à la place de le copier bêtement dans le cours.
from math import *
#La bibliothèque "math" nous permet d'ajouter le module "*" qui sera nécessaire pour faire comprendre le code à l'ordinateur.
import random
#Le module "random" (Aléatoire en français) nous permettra de choisir une valeur au hasard.Dans ce cas-ci, ce sera une valeur entre 1 et 100 qui sera par ailleurs la réponse.
x = random.randint(1,(100))
#Le jeu vous amuse ? Vous pouvez changer la marge des 1 et 100 en modifiant les nombres ci-dessus. 
e = int(input("Devinez le nombre entre 1 et 100."))
n = 1
#"n" est une variable qui permettra de déterminer notre nombre d'essais. Comme en mathématiques, son nom peut être modifié à votre guise.
while e != x :
        if e < x :
                print('Plus grand,')
                e = int(input('réessayez.'))
                n = n + 1
        if e > x :
                print ("Plus petit,")
                e = int(input('réessayez.'))
                n = n + 1
else :
	print("Vous avez gagné en", n, "essais.")
#IMPORTANT : Pour démarrer le programme, vous devez toujours passer par IDLE(ce programme) et cliquer sur le bouton F5. Cliquer directement sur le fichier le transformera en executable (.exe). Vu que le code n'est pas fait pour, le programme se fermera automatiquement après avoir réussi. Si vous utilisez cette méthode, vous risquez d'endommager le code du programme.
