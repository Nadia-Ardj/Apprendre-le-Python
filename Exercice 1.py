def main():
    #recolter une vaeur porte mannaie
    #creer un produit qui aura pour valeur 50
    #afficher la nouvelle valeur du porte monnaie, apres son achat

    monnaie = int (input("entrer le nombre d'£ que vous possedez dans votre porte monnaie"))
    print("vous avez actuellement ", monnaie, " euros")

    produit = 50
    print("le produit vaut ", produit , "euros")

    reste = monnaie - produit
    print("il vous reste ", reste , "euros")








if __name__ == '__main__' :
    main()