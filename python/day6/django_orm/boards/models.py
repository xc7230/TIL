from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField() #db에서 글자수 제한이 안된다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : {self.title}'


class Subway(models.Model):
    title = models.CharField(max_length=10)
    name = models.TextField(max_length=20)
    date = models.DateTimeField()
    sandwitch = models.CharField(max_length=10)
    size = models.IntegerField()
    bread = models.CharField(max_length=10)
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} : 이름은:{self.name}, 샌드위치는:{self.sandwitch}, 사이즈는:{self.size}, 소스는:{self.source}'