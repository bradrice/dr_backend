from django.db import models
from artwork.models import Artwork
from common import util

# Create your models here.

class AboutPageContent(models.Model):
    abouttitle = models.CharField(max_length=200, verbose_name="About Page Title")
    artwork = models.ForeignKey(Artwork, verbose_name="Artwork to show on Home page", on_delete=models.CASCADE)
    bodycontent = models.TextField(verbose_name="Body Content for About Page", blank=True, null=True)

    def clean(self):
        util.validate_only_one_instance(self)
    
    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'

    def __str__(self):
        return self.abouttitle