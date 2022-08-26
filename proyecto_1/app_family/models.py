from django.db import models

class familiar(models.Model):
  nombre=models.CharField(max_length=50)
  relacion=models.CharField(max_length=50)
  nacimiento=models.DateField()
  edad=models.IntegerField()
 