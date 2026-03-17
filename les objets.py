
"""class player :
    pseudo = "Nadia"
    health = 20
    attack = 3"

player1 = player()
print("Bienvenue au jouer ", player1.pseudo)

player2 = player()
print("Bienvenue au jouer ", player2.pseudo)"""
#là c'est le meme pseudo qui sera répéter , et pour se diff  on modifie la class :
class player :
    def __init__(self, pseudo , health , attack ):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au jouer ",pseudo , "/Points de vie:" ,health , "/attack: ", attack  )

    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def damage(self,damage):
        self.health -= damage

    def attack_player( self, cible):
         cible.damage(self.attack)


player1 = player("Nadia" , 20 ,3)
"""player1.damage(3)
print("Aie ...vous venez de subir " , damage , "dégats !")
print("Pseudo: ", player1.get_pseudo())
print("Health:" , player1.get_health())
print("Attack:", player1.get_attack())
print("vous possédez désormais", player1.get_health() , "points de vie ")"""

player2 = player("BOB ", 20 , 5)

player1.attack_player(player2)
print(player1.get_pseudo() ,"attaque", player2.get_pseudo())
print("Bienvenue au jouer ", player1.get_pseudo(), "/Points de vie:", player1.get_health(), "/attack: ", player1.get_attack())
print("Bienvenue au jouer ", player2.get_pseudo(), "/Points de vie:", player2.get_health(), "/attack: ", player2.get_attack())


