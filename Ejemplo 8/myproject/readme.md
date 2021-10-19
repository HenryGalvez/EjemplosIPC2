# Crear un nuevo proyecto de Django
> python -m django startproject <nombre projecto>  

ó
> django-admin startproject <nombre projecto>  

# Ejecutar el servidor de prueba de Django
> python manage.py runserver
# Crear una nueva app al proyecto
> python manage.py startapp <nombre app>
* modificar archivo settings.py en INSTALLED_APP y añadir el nombre de la app creada
# Añadiendo una nueva vista
En el archivo views.py de nuestra app importar lo siguiente:
> from django.http import HttpResponse   

En el mismo archivo crear un metodo que servira para enviar la respuesta al navegador sobre lo que tiene que verse en este caso el metodo se llamara signin
```
def sigin(request):
    return HttpResponse("Signin")
```
# Configurando las rutas de la app
En la nueva app crear un archivo llamado:
> urls.py  

Dentro del archivo escribir lo siguiente:
```
from django.urls import path
from .views import sigin

urlpatterns = [
    path('', sigin, name='home'),
]
```
del metodo path vemos lo siguiente:
* El primer parametro corresponde a la URL que tendra la vista
* El segundo parametro es la funcion que se encarga de dar la vista a mostrar
* El tercer parametro es el identificador que tendra la vista para usar en las redireccones

# Configurando las rutas del proyecto
En la carpeta del proyecto buscar el archivo
> urls.py  

Editarlo para que se vea como lo siguiente:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
```

De aca podemos notar:
* Se importo el metodo include() de django urls
* El metodo path soporta la url en donde se renderzara nuestra nueva app e incluimos todas sus vistas

# Creación de un modelo
En el archivo models.py de nuestra app podemos escribir clases que seran mapeadas a tablas en la base de datos configurada, por defecto es Sqlite3
un modelo puede verse de la siguiente manera:
```
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    pass
```
Luego se debe registrar el modelo en el archivo admin.py siempre en la app creada previamente
```
from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.register(Todo)
```
De este archivo podemos ver que importamos los modelos que creamos y mediente
> admin.site.register  

Los añadimos al administrador de Django

# Uso del administrador de Django
Primero para ver reflejados los modelos en el administrador hay que ingresar los siguientes comandos:
> python manage.py makemigrations  

> python manage.py migrate  

Estos comandos sirven para inciar el proceso de mapeo entre los modelos y las tablas en la base de datos  

Luego hay que crear un usuario adminstrador esto se hace con el comando:
> python manage.py createsuperuser  

Luego se configura un usuario y una contraseña  

El administrador estara disponible en la url
> /admin