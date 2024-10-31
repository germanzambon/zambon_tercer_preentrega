from django.db import models

class remera(models.Model):
    color= models.CharField(max_length=20)
    talle= models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.id} {self.color} {self.talle}"

    
