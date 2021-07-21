from _ast import arg

from django.db import models
from Subject_Category.models import Subject_Category
# Create your models here.
from django.urls import reverse


class product(models.Model):
    product_name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photo/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    cat_name = models.ForeignKey(Subject_Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('products_details', args=[self.cat_name.Slug, self.slug])

    def __str__(self):
        return self.product_name
