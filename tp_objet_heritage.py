#simulateur de ville
#créer 3 classes: immeuble, Supermarché et Banque
#Superclacc Batiment
# 4 immeubles , 2 supermarché et 1 banque

class batiment:
    def __init__(self, adresse , nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etages(self):
        return self.nb_etages

class immeuble(batiment):
    def __init__(self,adresse , nb_etages , nb_balcons):
        batiment.__init__(self , adresse , nb_etages)
        self.nb_balcons = nb_balcons

    def get_nb_balcons(self):
        return self.nb_balcons

class supermarche(batiment):
    def __init__(self, adresse, nb_etages, nb_rayons):
        batiment.__init__(self, adresse, nb_etages)
        self.nb_rayons = nb_rayons

    def get_nb_rayons(self):
        return self.nb_rayons

class banque(batiment):
    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        batiment.__init__(self, adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom

    def get_nb_coffres(self):
        return self.nb_coffres

    def get_nom(self):
        return self.nom

# 4 immeubles
immeuble1 = immeuble("26 rue de la gravenade", 3,3)
immeuble2 = immeuble("28 rue de la gravenade", 5,6)
immeuble3 = immeuble("78 rue elois mitterand", 2,2)
immeuble4 = immeuble("97 rue de la passiance", 8,4)

# 2 supermarché
supermarche1 = supermarche("27 rue de la foule", 4,12)
supermarche2 = supermarche("67 rue des rois", 8,27)

# 1 banque
banque = banque("23 rue piere", 6, 32 , "BnArdj")