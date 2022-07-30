from unicodedata import category
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

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
    image1 = VersatileImageField('Image',upload_to='images/work/', null=True)
    image2 = VersatileImageField('Image',upload_to='images/work/', null=True, blank=True)
    image3 = VersatileImageField('Image',upload_to='images/work/', null=True, blank=True)
    image4 = VersatileImageField('Image',upload_to='images/work/', null=True, blank=True)
   
    details = models.TextField()
    info = HTMLField()
    date = models.DateField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = ("Works")
        
    def __str__(self):
        return str(self.project_name)
   
    