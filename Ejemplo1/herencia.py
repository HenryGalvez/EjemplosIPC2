class Padre:
    def metodo1 (self):
        print("Metodo1")


t = Padre()

t.metodo1()

class Hijo(Padre):
    def metodo2(self):
        print("Metodo 2")


t2 = Hijo()

t2.metodo2()
t2.metodo1()

from abc import ABC, abstractclassmethod # Modulo Abstract Base Classes

class Expresion(ABC):
    @abstractclassmethod
    def operar(self):
        pass

class Aritmetica(Expresion) :
    def test(self):
        pass

    def operar(self, operacion, x, y):
        if(operacion == '+') :
            return x + y
        elif(operacion == '-') :
            return x - y
        elif(operacion == '*') :
            return x * y

class Relacional(Expresion) :
    def test(self):
        pass

    def operar(self, operacion, x, y):
        if(operacion == '<') :
            return x < y
        elif(operacion == '>') :
            return x > y
        elif(operacion == '==') :
            return x == y
        

arim = Aritmetica()
rel = Relacional()
print(arim.operar('+', 100, 50))
print(rel.operar('<', 100, 50))
print(rel.operar('>', 100, 50))
print(rel.operar('==', 100, 50))

obj = [1,2,3,4,5]

obj.pop()

print(obj)
print(type(obj))