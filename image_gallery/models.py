from django.db import models


# Create your models here.
class Celebrity(models.Model):
    name = models.CharField(max_length=100)


class Image(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    image = models.ImageField()

