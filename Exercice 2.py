#exercice pour s'enrainer au conditions :

#place de cinema
#recolter l'age de la personne
#si elle est mineur elle paye 7£
#si la personne est majeur -> 12£
#demander lui : souhaitez-vous du popcorn ?
#si oui -> +5£
#afficher le prix total à payer


age = int (input( " quel age avez-vous ?"))
if age < 18 :
    prix_a_payer = 7
else :
    prix_a_payer = 12
#ou alors en ternaire
#prix_a_payer = (7,12)[age<18]

reponse = input(" Souhaitez_vous du popcorn ? (oui,non)")

if reponse == "oui" :
    prix_a_payer = prix_a_payer + 5

print("Le prix total à payer est : ", prix_a_payer , "£")
