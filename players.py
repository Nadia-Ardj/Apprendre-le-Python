from enum import nonmember


class player :
    def __init__(self, pseudo , health , attack ):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au jouer ",pseudo , "/Points de vie:" ,health , "/attack: ", attack  )

    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def damage(self,damage):
        self.health -= damage

    def attack_player( self, cible, damage ):
        if self.has_weapon():
            damage += self.weapon.get_damage()
        cible.damage(self.attack)

    def change_weapon(self, weapon):
        self.weapon = weapon

    #verifier si le jouer a une arme :
    def has_weapon(self):
        return self.weapon is not None