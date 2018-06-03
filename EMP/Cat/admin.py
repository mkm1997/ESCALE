from django.contrib import admin
from .models import Product,Category,SubCategory,SubSubcate

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubSubcate)
admin.site.register(SubCategory)
