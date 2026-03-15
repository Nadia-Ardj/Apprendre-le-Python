import statistics
from random import  shuffle

#creér une liste qui vas stoker des pseudos pour simuler  un jeux en ligne
# Graven , Anana , Alex ...
online_players = [ "Graven" , "Anana" , "Alex"]
print(online_players)

#comment récuperer un élément dans la liste
print(online_players[0])
print(online_players[2])
print(online_players[len(online_players) -1])

#modifier les éléments
online_players[0] = "Gravenilvec"
#injecter un élément entre Anana et Alex
online_players.insert(2,"Bernart")
online_players[2:4] = ["Paul" , "Jack"]

#ajouter d'autres
online_players.append("Gamer123")
online_players.extend(["pierre" , "Bob"])
#n veut qu'un joueur dans la liste se deconnecte
online_players.pop(1)
del online_players[1]
online_players.remove("Gamer123")

#remettre à neuf votre liste
del online_players[:]
online_players.clear()


print(online_players)

#exemple : Jouer à la maitresse

notes = [ 8 , 12 , 17 , 18 , 15]
print(notes)
shuffle(notes)
print(notes)

#module : statistics
result = statistics.mean(notes)
print(" la moyenne de l'élève est  de {}".format(result))


#creer un autre liste /
text = input("Entrer une chaine de la forme (email-pseudo-motdepass)").split("-")
print(text)

print("salut {} , ton email {} , ton mot de pass {}".format(text[1],text[0] , text[2]))
