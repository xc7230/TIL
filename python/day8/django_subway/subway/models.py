from django.db import models

# Create your models here.

class Subway(models.Model):
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    menu = models.CharField(max_length=20)
    bread = models.CharField(max_length=10)
    vegetalbe = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    drink = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.name} : {self.menu}'