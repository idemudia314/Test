from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 250)
    subt = models.CharField(max_length= 250)
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title
