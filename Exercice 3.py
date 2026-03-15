from random import shuffle
#Generateur de phrases

#demander en console une chaine de la forme "mot1/mt2/mot3 ..."
#tronsformer cette chaine en liste et la melanger
#si le nombre d'éléments de la liste est < 10
#->afficher les deux premiers mots
#si le nombre d'élements est >= 10
#-> afficher les 3 derniers

chaine = input(" entrer une chaine de la forme mot1/mot2/mot3").split("/")
print(chaine)
shuffle(chaine)
print(chaine)

chaine_len = len(chaine)
if chaine_len < 10 :
    print(chaine[0:2])
elif chaine_len >= 10 :
    print(chaine[chaine_len-3:chaine_len])

