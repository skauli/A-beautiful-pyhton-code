import random

def resultOk():
    print("Richtig, Du hast " + str(count) + "  Versuch(e) benötigt!")
    moveOn = input('Noch eine Aufgabe? Gebe (genau!) "j" für "JA" oder "n" für "NEIN" ein: ')
    while moveOn != "j" and moveOn != "n":
        moveOn = input('Gebe"j" für "JA" oder "n" für "NEIN" ein: ')
    if moveOn == "nein":
        print("Tschau")
        exit()
        
while True:
    number1 = random.randint(50,100)
    number2 = random.randint(0,number1-1)   
    count = 0

    print("Was ist {} + {} ?".format(str(number1), str(number2))) 
    resultInput = int(input("Deine Lösung?: "))
    resultCalc = number1 - number2
    if resultInput == resultCalc:
        count += 1
        resultOk()
    while resultInput != resultCalc:
        count += 1
        print("leider falsch, nochmal!")
        resultInput = int(input("Deine Lösung? : "))
        if resultInput == resultCalc:
            count += 1
            resultOk()
            
print("I' am so happy")
print("are you")
print("difficult")
print("Änderung 4")
