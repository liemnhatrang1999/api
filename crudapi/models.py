from pyexpat import model
from django.db import models

class Product(models.Model):
    
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    quantite = models.IntegerField()

    def __str__(self) :
        return (self.id)