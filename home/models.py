from django.db import models
from artwork.models import Artwork
from django.core.exceptions import ValidationError
from common import util
# Create your models here.

class HomePageContent(models.Model):
    hometitle = models.CharField(max_length=200, verbose_name="Home Page Title")
    artwork = models.ForeignKey(Artwork, verbose_name="Artwork to show on Home page", on_delete=models.CASCADE)
    bodycontent = models.TextField(verbose_name="Body Content for Home Page", null=True, blank=True)
    
    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'

    def __str__(self):
        return self.hometitle