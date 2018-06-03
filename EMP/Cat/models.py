from django.db import models

# Create your models here.



class Product(models.Model):
    Product_id = models.IntegerField()

    product_name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.product_name


class Category(models.Model):
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    cat_id = models.IntegerField()
    Cat_name = models.CharField(max_length=100)


class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    SubCat_id = models.IntegerField()
    SubCat_name = models.CharField(max_length=100)

class SubSubcate(models.Model):
    subcat_id = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    Ssubcat_id = models.IntegerField()
    Ssubcat_name=models.CharField(max_length=100)

