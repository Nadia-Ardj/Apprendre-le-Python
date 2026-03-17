def welcome():
    print("welcome!")
    result = 5 + 6
    print("le calcul du resultat est :" , result)

welcome()  # on oeut appeler la fonction combien de fois qu'on veut

def next_year():
    global year
    print("fin de l'année " , year)
    year += 1
    print(" debut de l'année" , year )
year = 2018
next_year()
next_year()

# fonction addition

def addition():
    result = 5 + 5
    return result

#mult
def multply():
    result = 5*4
    return result

def addition1():
   return 5 + 4

def addition2():
   return 5 + 9
def get_message():
    return "le resultat du calcul est : "
print(get_message(), addition())
print(get_message(), addition1())
print(get_message(), addition2())
print(get_message(), multply())


# au lieu de réecrire la fonction à plusiers rep on utilise un paramétre :
def addition(n):
    return  5 + n
print(get_message(), addition(5))

#créer une fonction qui va renvoyer le resultat le plus haut parmis 2 valeurs

def max(a , b ):
   if a > b : return a
   else: return b

a = int(input("a ="))
b = int(input("b ="))
print("le max est : " ,max(a,b))

#récursivité :
def add(a):
    a += 1
    print(a)
    if a < 10 :
      add(a)

add(2)