from django.shortcuts import render
from .models import SubCategory,Product,SubSubcate,Category

# Create your views here.
def index(request):

    product = Product.objects.get(Product_id=1)
    print(product.Product_id,product.product_name)

    p=product.Product_id

    category = Category.objects.get(Product_id=p)
    print(category.cat_id,category.Cat_name)

    subcategory = SubCategory.objects.get(cat_id=category.cat_id)
    print(subcategory.SubCat_id, subcategory.SubCat_name)
    subSubcategory = SubSubcate.objects.get(subcat_id=subcategory.SubCat_id)
    print(subSubcategory.Ssubcat_id,subSubcategory.Ssubcat_name)



    return render(request,'Index.html',{'product':product})


#'cat':category,'sub':subcategory,'ssub':subSubcategory