text = ""

import xml.etree.ElementTree as ET
from xml.dom import minidom

def primeraFuncion():
    print("Primera funcion")
    path = input("Ingrese la ruta del archivo: ")
    try:
        file = open(path)
        global text
        text = file.read()
        print("Exito!!!")
    except:
        print("Ruta invalida")


def segundaFuncion():
    print("Segunda funcion")
    global text
    print(text)

def salirFuncion():
    quit()

def elementtreeFuncion():
    tree = ET.parse("zoo.xml")
    root = tree.getroot()

    print("\nTodos los atributos")
    for elemento in root:
        for subelemento in elemento:
            print(subelemento.attrib)
    
    for elemento in root:
        print(elemento.tag)
        for subelemento in elemento:
            print(">",subelemento.text)
    
    print("\nUnico Elemento")
    print(root[1][0].text)

    print("Cantidad")
    print(len(root[0]))

    data = ET.Element('data')
    item1 = ET.SubElement(data,'items')
    item2 = ET.SubElement(data,'items')
    item1.set('name',"item1")
    item2.set('name',"item2")
    item1.text = "item1 abc"
    item2.text = "item2 abc"

    mydata = ET.tostring(data,"unicode", "xml")
    myfile = open("item2.xml", "w")
    myfile.write(mydata)

    print("\nMetodo FindAll")
    for elemento in root:
        for subelemento in elemento.findall('animal'):
            print(subelemento.attrib)
            print(subelemento.get('recinto'))
            subelemento.set('recinto', "Modificado")
            subelemento.set('recintoP', "Si")
    tree.write('newzoo.xml')

def minidomFuncion():
    mydoc = minidom.parse('items.xml')
    items = mydoc.getElementsByTagName('item')

    print('Valor de Atributos de elementos:')
    print(items[0].attributes['name'].value)

    for e in items:
        print(e.attributes['name'].value)

    print("forma 1:", items[0].childNodes[0].data)
    print("forma 2:", items[0].firstChild.data)