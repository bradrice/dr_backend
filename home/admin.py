from django.contrib import admin
from .models import HomePageContent


class HomeAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(HomePageContent, HomeAdmin)