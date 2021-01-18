from django.contrib import admin
from .models import AboutPageContent


class AboutAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(AboutPageContent, AboutAdmin)