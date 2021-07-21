from django.contrib import admin
from . models import product

# Register your models here.


class product_Admin(admin.ModelAdmin):
    list_display = ('product_name',
                    'price',
                    'stock',
                    'cat_name',
                    'modified_date',
                    'is_available')
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(product, product_Admin)