from django.contrib import admin
from .models import Artwork, Category
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
class ArtworkAdmin(SortableAdminMixin, admin.ModelAdmin):
    js = ('js/form.js',)
    list_display = ('title', 'weightedOrder', 'forSale', 'sold', 'media', 'price')
    readonly_fields = ('imgheight', 'imgwidth')
    
    # class Meta: 
    #     fields = ('artimage', 'title', 'media', 'description', 'created', 'width', 'height', 'forSale', 'sold', 'price', 'showOnWebsite', 'category')
    #     exclude = ('imgheight', 'imgwidth')

admin.site.register(Artwork, ArtworkAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)
