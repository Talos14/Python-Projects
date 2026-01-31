print("================================================")
print("ALTERRA Calculators Inc.")
print("Precision, Productivity, Profit!")
print()
#Main Calculator Stuff begins here.
print("==================")
print("Area Calculator 📐")
print("==================")
print()
#Choices...choices so many choices
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print()
#Mirror...mirror pray heed my call, who is the shape that is the best of all.
userInput = int(input("Which shape: "))
print()

if userInput == 1:
    #Triangle Mafia of Lost Heaven City      
    userBase = int(input("Base: "))
    userHeight = int(input("Height: "))
    calcTriArea = (userBase*userHeight)/2
    print()
    print("The area is ",calcTriArea)
elif userInput == 2:
    #Rectangle Mob of Empire Bay
    userLength = int(input("Length: "))
    userWidth = int(input("Width: "))
    calcRectArea = userLength*userWidth
    print()
    print("The area is ",calcRectArea)
elif userInput == 3:
    #Square Mob of Old Country
    userSide = int(input("Side: "))
    calcSquareArea = userSide**2
    print()
    print("The area is ",calcSquareArea)
elif userInput == 4:
    #Circle Mafia of New Bordeaux
    userRadius = int(input("Radius: "))
    calcCircleArea = 3.14 * (userRadius**2)
    print()
    print("The area is ",calcCircleArea)
elif userInput == 5:
    #Exit Clause
    print()
    print("Exiting Calculator...")
else:
    #For when you do a dum dum
    print()
    print("Invalid Parameters")

#Totally Not Related to Subnautica ALTERRA. Absolutley not.
print()
print("Thank You for using ALTERRA Calculators")
print("ALTERRA Inc. - A better, more productive future.")
print("================================================")

