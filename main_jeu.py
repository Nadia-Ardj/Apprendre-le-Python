
from players import player
from weapon import weapon

knife = weapon("couteau" , 3)

player1 = player("Nadia" , 20 ,3)
player2 = player("BOB ", 20 , 5)
player1.change_weapon(knife)

player1.attack_player(player2)
print(player1.get_pseudo() ,"attaque", player2.get_pseudo())
print("Bienvenue au jouer ", player1.get_pseudo(), "/Points de vie:", player1.get_health(), "/attack: ", player1.get_attack())
print("Bienvenue au jouer ", player2.get_pseudo(), "/Points de vie:", player2.get_health(), "/attack: ", player2.get_attack())


