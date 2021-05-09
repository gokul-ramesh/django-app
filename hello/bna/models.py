from django.db import models

# Create your models here.
from django.db import models


class author(models.Model):
    name= models.CharField(max_length=50)

class book(models.Model):
    name= models.CharField(max_length=50)
    author=models.ForeignKey(author,on_delete=models.CASCADE,default=1)