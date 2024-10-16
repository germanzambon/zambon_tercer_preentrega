from django.db import models

class zapatillas(models.Model):
    marca=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    talle=models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.color} {self.talle}"
