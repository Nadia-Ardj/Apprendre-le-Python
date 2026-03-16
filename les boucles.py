from calendar import month

print("vous etes le client n°1")
#for : pour une valeur de départ (1) jusqu'à une valeur d'arrivé(5)
for i in range(1,5):
    print("vous etes le client n°",i)
#for each : pour chaque valeur d'une liste données
print("Email envoyé à : gravenin@gail.com")
print("Email envoyé à : gravenkb@gmail.com")
#utiliser la boucle :
emails = ["gravennt@gmail.com" , "gravenin@gail.com" , "contact@gmail.com"]
#blacklist
blacklist = ["gravendev@free.fr" , "gravenin@gail.com", "contact@gmail.com"]
#pour chacune des valeurs j'affiche "Email envoyé à [email]
for email in emails :

    if email in blacklist :
       print("Email {} interdit ! envoi impossible !".format(email))
       continue
       print("Email envoyé à : ", email)
#while : tant qu'une condition est vrai
#salarié 1500 £ / mois
salary = 1500
#tant que le salaire < 2000£ , +120£
while salary < 2000 :
    salary += 120
    print("votre salaire actuel est de : " , salary , "£")
    print("fin de la boucle  ")

#exemple d'un youtubeur "Graven" , 2500 abonnées
susctibers_count = 2500
#il gagne 10% d'audiance supplementaire par mois
month = 0
#on souhaite estimer combien aura t'il d'abonnés , aprés 2 ans ( 24 mois )
while month <= 24 :
    #augmenter l'audiebce
    # + 30% : 1 + (30/100) : 1.3
    # -20% : 1 - (20/100) : 0.8
    susctibers_count  *= 1.10
print("vous avez actuellement {} abonnés ".format(susctibers_count))
#on passe au mois suivant :
month +=1
