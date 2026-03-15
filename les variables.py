def main():
    #premièrement le nom de la variable , il ne faut pas qu'il contient des espaces, tout est minuscule, et y'a pas de caractéres spéciaux comme %@#
    #ça serai mieux d'écrire en anglais l'intégralité du nom
    #aprés le nom en écrit "=" pour affecter une valeur à la variable , et pour les chaines de caractères on le met entre " "exp : name_user = "graven"
    #creation des variables :
    username = "Graven"
    age = 19
    wallet = 187.6
    #des variables avec type booléén , il nous donne deux possibilité de reponse soit : True or False
    is_happy = True
    #affichage des variables :
    print(username)

    age = 19
    print(username, age)


# change la valeur la valeur age avec 25
age = 25
print(age)
age = age + 1
username = "Alex"
print("salut" + username + "vous avez " + str(age) + "ans")


    if __name__ == '__main__':
        main()


