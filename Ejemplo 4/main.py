from datetime import datetime
import re

class RH:
    empleados = {}
    log = ()

    def ingresar_empleado(self, _dpi, _nombre, _genero, _edad):
        self.empleados[_dpi] = {
            "nombre": _nombre,
            "genero": _genero,
            "edad": _edad
        }
        self.log = self.log + (("Accion: INGRESO", "DPI:"+str(_dpi),"Fecha: "+str(datetime.now())),)
        pass

    def imprimir_empleados(self):
        for empleado in self.empleados:
            print(empleado, ":", self.empleados[empleado])
        print("")
        pass

    def eliminar_empleado(self, _dpi):
        print("Se elimino", _dpi, self.empleados.pop(_dpi))
        self.log = self.log + (("Accion: ELIMINACION", "DPI:"+str(_dpi),"Fecha: "+str(datetime.now())),)
        pass
    
    def editar_nombre_empleado(self,_dpi, _nuevo_nombre):
        self.empleados[_dpi]["nombre"] = _nuevo_nombre
        print("Se edito",_dpi, self.empleados.get(_dpi))
        self.log = self.log + (("Accion: EDICION", "DPI:"+str(_dpi),"Fecha: "+str(datetime.now())),)
        pass

    def imprimir_log(self):
        for l in self.log:
            print(l)
        print("")
        pass

    def obtener_empleado(self, _patron):
        ret = []
        for empleado in self.empleados:
            res = re.search(_patron, self.empleados[empleado]["nombre"])
            if not(res == None):
                ret.append(self.empleados[empleado])
        return ret
        pass

mytemp = RH()

mytemp.ingresar_empleado(1,"Kevin", "M", "25")
mytemp.imprimir_empleados()
mytemp.ingresar_empleado(2,"Sara", "F", "20")
mytemp.imprimir_empleados()
mytemp.eliminar_empleado(2)
mytemp.imprimir_empleados()
mytemp.editar_nombre_empleado(1,"Oscar")
mytemp.imprimir_empleados()

mytemp.imprimir_log()

# 1231238881238923791888888273897129837892
# 8+
# 12345
# 5?
# 8+ | 5?

mytemp.ingresar_empleado(2,"Kevin","M","25")
mytemp.ingresar_empleado(3,"Kara","F","21")
mytemp.imprimir_empleados()
print(mytemp.obtener_empleado("K[a-z]+"))

cadena = "24/02/2021"
mat = re.match("(\d{2})[/](\d{2})[/](\d{4})",cadena)
print(mat)
print("")

cadena = "ss/02/2021"
mat = re.match("(\w{2})[/](\d{2})[/](\d{4})",cadena)
print(mat)
print("")

cadena = "8henry"
mat = re.match("[a-zA-z][\w]*",cadena)
print(mat)
print("")