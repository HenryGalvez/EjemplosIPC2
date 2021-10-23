from django.contrib import admin
from .models import Todo, Survey


# Register your models here.
admin.site.register(Todo)
admin.site.register(Survey)