from Nodo import Nodo
class Lista:
    def __init__(self):
        self.primer = None
        self.ultimo = None
        self.tamaño = 0
        self.iterador = 0

    def insertarUltimo(self, _valor):
        if(self.ultimo == None):
            self.ultimo = Nodo(_valor)
            self.primer = self.ultimo
            self.tamaño += 1
            return True
        else:
            temporalNodo = Nodo(_valor)
            self.ultimo.siguiente = temporalNodo
            # codigo para doblemente enlazado
            # temporalNodo.anterio = self.ultimo

            self.ultimo = temporalNodo

            # Codigo para circular
            # self.ultimo.siguiente = self.primer

            self.tamaño += 1
            return True
        return False
        pass

    def buscarEnLista(self, _key):
        if(_key < 0 or _key > self.tamaño - 1):
            print("Error, Fuera de rango")
            return None
        if(self.ultimo == None):
            print("Error, Lista vacia")
            return None
        
        temporalNodo = self.primer
        for i in range(0, _key, 1):
            temporalNodo = temporalNodo.siguiente
        return temporalNodo
        pass

    def eliminarUltimo(self):
        temp = self.buscarEnLista(self.tamaño-2)
        tempReturn = temp.siguiente
        temp.siguiente = None
        self.ultimo = temp
        self.tamaño -=1
        return tempReturn.valor
    
    def __getitem__(self, _key):
        tempReturn = self.buscarEnLista(_key)
        return tempReturn.valor if tempReturn != None else None # <condicion> ? retVerdadero : retFalse
    
    def __setitem__(self, _key, _nuevoValor):
        tempReturn = self.buscarEnLista(_key)
        if(tempReturn != None):
            tempReturn.valor = _nuevoValor
        pass

    def __iter__(self):
        self.iterador = 0
        return self

    def __next__(self):
        if self.iterador == self.tamaño :
            raise StopIteration
        self.iterador += 1
        return self.buscarEnLista(self.iterador-1).valor
        pass