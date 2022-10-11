from tkinter.tix import Tree
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    descrition = models.TextField(default="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)
