# hight1 = 1.83
# hight2 = 2.03
# hight3 = 1.70

# if (hight1 > hight2):
#     print(f"hight 1 is {hight1}")
# else:
#     print(f"hight 2 is {hight2}")

# snow = True
# monday = False

# if monday & snow:
#     print("im staying home")

# sport = "cycling"

# match sport:
#     case "track and field":
#         print("i use to play a lot of sport")
#     case "badminton":
#         print("i suck at badminton")
#     case "cycling":
#         print("financialy a bad descision")
#     case _:
#         print("sport isn't realy my thing")
def calculatrice (nbg, nbd, symb):
    nombre_a_gauche = nbg
    nombre_a_droite = nbd
    symbole = symb
    resultat = 0

    if ((type(nombre_a_gauche) != int | type(nombre_a_droite) != int)):
        return("One or more variable is a float")
    if(nombre_a_droite == 0 and symbole == '/'):
        return("cannot divide by zero")
    
    match symbole:
        case "+":
            return(nombre_a_gauche + nombre_a_droite)
        case "-":
            return(nombre_a_gauche - nombre_a_droite)
        case "*":
            return(nombre_a_gauche * nombre_a_droite)
        case "/":
            return(nombre_a_gauche / nombre_a_droite)
        case _:
            return("sybole do not match")
        

print(calculatrice(10, 0, "/"))