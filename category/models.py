from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE)

    class Meta:

        def __str__(self):                           
            return self.name