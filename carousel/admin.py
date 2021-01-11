from django.contrib import admin
from .models import Carousel
# from artwork.models import Artwork

# Register your models here.

# class ArtworkInline(admin.TabularInline):
#     model = Artwork

class CarouselAdmin(admin.ModelAdmin):
    pass
    


admin.site.register(Carousel, CarouselAdmin)