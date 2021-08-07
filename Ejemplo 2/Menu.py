from MenuOption import *
from Functions import *

from colorama import Fore, Back, Style


class Menu:
    options = []

    def __init__(self):
        self.addMenuOption("Imprimir Archivo", primeraFuncion)
        self.addMenuOption("Leer Archivo", segundaFuncion)
        self.addMenuOption("XML con Element Tree", elementtreeFuncion)
        self.addMenuOption("XML con Mini Dom", minidomFuncion)
        self.addMenuOption("Salir", salirFuncion)
        pass

    def addMenuOption(self, text, function):
        self.options.append(MenuOption(text, function))

    def executionMenuOption(self, key):
        self.options[key].execute()
    
    def printMenu(self):
        print(Style.BRIGHT)
        print(Fore.MAGENTA, "*****",Fore.BLUE,"Bienvenido, por favor elija una opcion")
        for i, opt in enumerate(self.options):
            print(i,"-", opt.text)
        print(Fore.MAGENTA,"*****", Style.RESET_ALL)