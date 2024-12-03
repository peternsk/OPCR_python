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

# def calculatrice (nbg, nbd, symb):
#     nombre_a_gauche = nbg
#     nombre_a_droite = nbd
#     symbole = symb
#     resultat = 0

#     if ((type(nombre_a_gauche) != int | type(nombre_a_droite) != int)):
#         return("One or more variable is a float")
#     if(nombre_a_droite == 0 and symbole == '/'):
#         return("cannot divide by zero")
    
#     match symbole:
#         case "+":
#             return(nombre_a_gauche + nombre_a_droite)
#         case "-":
#             return(nombre_a_gauche - nombre_a_droite)
#         case "*":
#             return(nombre_a_gauche * nombre_a_droite)
#         case "/":
#             return(nombre_a_gauche / nombre_a_droite)
#         case _:
#             return("sybole do not match")
        

# print(calculatrice(10, 0, "/"))

# nomEtudiant = ["zazou", "maggy", "denzel", "chloe", "pete"]
# for Etudiant in nomEtudiant:
#     if(Etudiant == "denzel"):
#         continue
#     print(Etudiant)


# nbTaco = 50
# nbTacoMange = 3

# while nbTacoMange <= nbTaco:
#     print(f"Peter a mange {nbTacoMange} tacos")
#     if(nbTacoMange > 11):
#         break;
#     nbTacoMange += 1

# def somme(list):
#     res = 0

#     for num in list:
#         res += num
#     return(res)

# def avrg(list):
#     res = 0;
#     if(len(list) <= 0):
#         return("cannot perform avrage calculation")
#     res = somme(list) / len(list)
#     return(res)

# def higher(list):
#     high_list = []

#     for num in list:
#         if(num <= avrg(list)):
#             continue
#         high_list.append(num)

#     print(high_list)

# def pair(list):
#     pair_list = []

#     for num in list:
#         if(num % 2 > 0):
#             continue
#         pair_list.append(num)

#     print(pair_list)


# def calculateList():
#     user_list = input('ENTER a list of number\n')
#     # print(f"[{user_list}]")

#     num_list = []

#     for char in user_list:
#         if(char == ','):
#             continue
#         num_list.append(int(char))
    
#     print(f"{num_list}")

#     print(somme(num_list))
#     print(int(avrg(num_list)))
#     higher(num_list)
#     pair(num_list)

    
# calculateList()

