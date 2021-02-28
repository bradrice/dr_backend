from django.contrib import admin
from .models import Sketchbook, Category


# Register your models here.
class SketchbookAdmin(admin.ModelAdmin):
    js = ('js/form.js',)
    list_display = ('title', 'showOnWebsite')
    readonly_fields = ('imgheight', 'imgwidth')
    
    # class Meta: 
    #     fields = ('artimage', 'title', 'media', 'description', 'created', 'width', 'height', 'forSale', 'sold', 'price', 'showOnWebsite', 'category')
    #     exclude = ('imgheight', 'imgwidth')

admin.site.register(Sketchbook, SketchbookAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)