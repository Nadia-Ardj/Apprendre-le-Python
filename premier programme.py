def main():
    #recolter une première note
    note1 = int (input("entrer ta premmière note "))
    #recolter la deuxieme note
    note2 = int (input("entrer une deuxieme note"))
    #recolter la troisième note
    note3 = int (input("entrer la derniere note"))
    #calculer la moyenne
    result = (note1 + note2 + note3)/3
    print("le moyenne de l'élève  est  " + str(result))



if __name__ == '__main__' :
    main()