from Menu import *

menu = Menu()



while(True):
    menu.printMenu()
    text = input()
    key = 0
    try:
        key = int(text)
    except:
        print("ERROR: Numero entero invalido")
        continue
    menu.executionMenuOption(key)