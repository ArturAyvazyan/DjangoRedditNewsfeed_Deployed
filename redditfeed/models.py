from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    text = models.TextField(max_length = 500)
    image = models.ImageField(verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True, blank=True)

    #class Meta:
    #    ordering = ['id']
    #video =  models.URLField(max_length=128, db_index=True, unique=True, blank=True)

