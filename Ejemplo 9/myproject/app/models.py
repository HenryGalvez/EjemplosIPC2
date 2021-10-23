from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

option = [
    [0, "Muy Malo"],
    [1, "Malo"],
    [2, "Aceptable"],
    [3, "Bueno"],
    [4, "Muy Bueno"]
]

class Survey(models.Model):
    isfrendly = models.BooleanField()
    opinion = models.TextField()
    qualification = models.IntegerField(choices=option)

    def __str__(self):
        return str(self.qualification)