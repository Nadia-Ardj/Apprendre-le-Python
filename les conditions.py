#code
wallet = 5000
computer_price = 1000

#verifier le prix de l'ordinateur est <  à 1000
print(computer_price < 1000)
if computer_price <= 1000:
    print(" l'achat est possible ")
    wallet -= computer_price
else :
    print("Non, vous ne pouver pas acheter cet ordinateur ")
print(wallet)

#les conditions ternaires
text = ("l'achat est possible" , "l'achat est impossible ")[computer_price <= 1000]
print(text)

#exemple : Systeme de verification de mot de passe
password = input("Entrer votre mot de passe")
password_length = len(password)
print(password_length)

#vérifier si le mot de passe est inférieur à 8 caractères :
if password_length <= 8 :
    print( " mot de passe trop court ! ")
elif password_length > 8  and password_length < 12:
    print( " mot de passe moyen !  ")
else :
    print( " mot de pass parfait !")