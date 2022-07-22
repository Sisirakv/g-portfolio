from unicodedata import category
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.title)
    


class Works(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/work/', null=True)
    details = models.TextField()
    date = models.DateField(editable=True)
    link = models.URLField()
    slug = models.SlugField(unique=True)
    
    
    class Meta:
        verbose_name_plural = ("Works")
        
    def __str__(self):
        return str(self.project_name)
    

class Gallery(models.Model):
    project_name = models.ForeignKey(Works, on_delete=models.CASCADE, null=True)
    image = VersatileImageField('Image',upload_to='images/gallery/')
    
    
    def __str__(self):
        return str(self.project_name)
    