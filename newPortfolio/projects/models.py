from django.db import models


# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=80)
    desc = models.CharField(max_length=200)
    imgUrl = models.ImageField(upload_to='projects/images')
    url = models.URLField(blank=True)

