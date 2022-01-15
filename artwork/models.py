from django.db import models

# from dr_backend.settings.base import *
from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.placeholder import OnStoragePlaceholderImage
# from carousel.models import Carousel

# Create your models here.

# def artwork_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    # return MEDIA_ROOT + '/artwork/{0}'.format(filename) 

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):                          
        return str(self.name)

class Artwork(models.Model):

    MEDIA_TYPES = (
        ('A', 'Acrylic'),
        ('W', 'Watercolor'),
        ('MM', 'Multimedia'),
        ('G', 'Gouache'),
        ('O', 'Oil'),
        ('P', 'Pencil'),
        ('C', 'Charcoal'),
        ('PS', 'Pastel'),
        ('CO', 'Conte Crayon'),
    )

    artimage = VersatileImageField(
        'Image',
        upload_to='artwork',
        width_field='imgwidth',
        height_field='imgheight',
        ppoi_field='ppoi',
        null=True,
        blank=True
    )
    ppoi = PPOIField(
        'Image PPOI'
    )
    imgheight = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Image Height (Pixels)"
    )
    imgwidth = models.PositiveIntegerField(
        verbose_name='Image Width (Pixels)',
        blank=True,
        null=True
    )
    title = models.CharField(max_length=200, default="Untitled")
    media = models.CharField(max_length=3, choices=MEDIA_TYPES)
    description = models.CharField(max_length=300, blank=True)
    entered_at = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    width = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Dimension width (inches)")
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Dimension height (inches)")
    forSale = models.BooleanField(null=False, default=False)
    sold = models.BooleanField(null=False, default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Price in US dollars")
    showOnWebsite = models.BooleanField(null=False, default=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    weightedOrder = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Artwork'
        verbose_name_plural = 'Artworks'
        ordering = ['weightedOrder']


    def __str__(self):
        return str(self.id) + " - " + self.title

    


