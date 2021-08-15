from Lista import Lista

lista = Lista()

lista.insertarUltimo(Lista())
lista.insertarUltimo(Lista())

lista.buscarEnLista(0).valor.insertarUltimo(1)
lista.buscarEnLista(0).valor.insertarUltimo(2)
lista.buscarEnLista(1).valor.insertarUltimo(3)
lista.buscarEnLista(1).valor.insertarUltimo(4)

#  1 2
#  3 4
print(lista.buscarEnLista(0).valor.buscarEnLista(0).valor) # lista[0][0] + * /
print(lista.buscarEnLista(0).valor.buscarEnLista(1).valor)

print(lista.buscarEnLista(1).valor.buscarEnLista(0).valor)
print(lista.buscarEnLista(1).valor.buscarEnLista(1).valor)

print("")
print(lista[1][0])
print(lista[1][1])

# lista[1][0] = 100
lista[1][0] = 100
print(lista[1][0])

l = Lista()
l.insertarUltimo(10)
l.insertarUltimo(11)
l.insertarUltimo(12)
l.insertarUltimo(13)

print("\nIterador")

for ite in l:
    print(ite)

print("Elemento eliminado", l.eliminarUltimo())

for ite in l:
    print(ite)

listP = [1,2,3,4,5,6]

print(listP[2])
print(listP[-2])