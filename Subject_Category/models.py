from django.db import models
from django.urls import reverse

# Create your models here.


class Subject_Category(models.Model):
    Cat_Name = models.CharField(max_length=50, unique=True)
    Slug = models.CharField(max_length=50, unique=True)
    Descreption = models.CharField(max_length=100, blank=True)
    Cat_Image=models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.Cat_Name

    def get_url(self):
        return reverse('products_by_category',args=[self.Slug])