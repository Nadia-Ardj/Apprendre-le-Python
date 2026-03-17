# tp sur les fonctions :

# unr fonction pour calculer le nombre de voyelles dans un mot
#créer un compteur de voyelles
#pour chaque lettre du mot vous verifier s'il s'agit d'une voyelle
#si le cas on ajoute 1 au compteur
#à la fin de la fonction vous renvoyer le compteur

mot = input("entrer un mot")
def count_voyelles(mot):
    cpt = 0
    for letter in mot:
        if  letter in ['a', 'e', 'i', 'o' , 'u' , 'y']:
            cpt += 1
    return cpt

print("il y'a ", count_voyelles(mot) , "voyelles dans le mot", mot)

