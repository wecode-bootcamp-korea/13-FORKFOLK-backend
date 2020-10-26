import json

from django.db.models          import Q
from django.views              import View
from django.views.generic.list import ListView

from django.http      import (
                        JsonResponse,
                        HttpResponse
                        )

from product.models   import (
                        ShopCategory,
                        Product,
                        RelatedProduct,
                        ProductImage,
                        Cart
                        )

class ShopAllView(View):
    def get(self,request):
        products = Product.objects.all()
        product_list = []
        product_dic = {}
        for product in products:
            name     = product.name
            price    = product.price 
            category = ShopCategory.objects.get(id=product.category_id)
            product_dic['name']     = name
            product_dic['category'] = category.name
            product_dic['price']    = price
            product_list.append(product_dic)
        return JsonResponse({'product_info':product_list},status=200)
