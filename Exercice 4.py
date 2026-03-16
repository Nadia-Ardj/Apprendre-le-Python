#jeu du juste prix :
# choisir un nombre entre 1 et 1000
# tant que le jeu n'est pas fini
#   -> demander à l'utilisateur d'entrer un prix
#   -> si il trouve le juste prix "c'est gagné"
#   -> sinon onaffiche " c'est moins " ou "c'est plus"
import random

just_prix = random.randint(1,1000)
running = True
while running :
    prix_sup = int(input("entrer un prix "))
    if just_prix == prix_sup :
        print(" Trouvé , c'est gagné !")
        running = False
    elif prix_sup < just_prix :
        print("c'est plus ")
    else :
        print("c'est moins ")

print("fin du jeu")