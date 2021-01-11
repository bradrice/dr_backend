from django.db import models
from artwork.models import Artwork

# Create your models here.

class Carousel(models.Model):
    carouseltitle = models.CharField(max_length=200,)
    artwork = models.ManyToManyField(Artwork)
    
    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self):
        return self.carouseltitle