# print("helloworld")
# print( 2 + 3)
# print( '2' + '3')

# helloworld = "ca fonction !"
# helloworld = 2 + 4

# print(helloworld)


# age1 = 30
# age2 = 29
# age3 = 1.8

# if(age2 + age3 > age1):{
#     print("we are older combine")
# }
# else:{
#     print("NVM")
# }

# print(f"age1 :{age1} age2 : {age2} age3 : {age3}")

# avrgSpeed = 50.7
# cyclisteName = "Peter"
# isHeTheBest = True

# print(type(avrgSpeed))
# print(type(cyclisteName))
# print(type(isHeTheBest))

# class person :
#     avrgSpeed = 50.7;
#     cyclisteName = "Peter";
#     isHeTheBest = True;

# def printPerson(person):
#     print(person.avrgSpeed)
#     print(person.cyclisteName)
#     print(person.isHeTheBest)

# def getType(person):
#     print(type(person.avrgSpeed))
#     print(type(person.cyclisteName))
#     print(type(person.isHeTheBest))

# printPerson(person)
# getType(person)

# peter = person
# maggy = person
# zazou = person
# classList = []

# classList.append(peter)
# classList.append(maggy)
# classList.append(zazou)
# print(classList[0].cyclisteName[0])
# print(classList[0].cyclisteName[-4])
# print(len(classList))

# print(classList)

# fruits = ["pomme", "banane", "orange"]

# fruits.append("kiwi")
# print(len(fruits))
# print(fruits)
# fruits.remove("orange")
# fruits[1] = "ananas"
# print(len(fruits))
# print(fruits)

entreprise = {
    "Directeur": "Peter malonge Nsaka",
    "Directeur commercial": "Zaya maltais nsaka",
    "Data de debut": "16/04/1994",
    "Data de fin": "16/04/2056",
    "Nombre d'employe": 4,
    "Profit annuel" : 180000000,
    "Siege social" : "Lusaka, Zambie",
}

# print(f" le directeur dentreprise est M. {entreprise['Directeur']} qui gere un profit net annuel de {entreprise['Profit annuel']}")

entreprise["CTO"] = "Magalie Maltais Laurence"

entreprise["Cuisinier"] = "Denzel"

# print(f" la nouvelle CTO est Mme. {entreprise['CTO']}")

del entreprise["Nombre d'employe"]

# print(entreprise.keys())
# print(entreprise.values())
print(entreprise)
if("Directeur" in entreprise):
    print("le post est non disponoble a l'embauche")