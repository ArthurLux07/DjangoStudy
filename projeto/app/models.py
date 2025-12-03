from django.db import models

class InfoCad(models.Model):
    nome = models.CharField(max_length=200)  
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.idade} anos"
