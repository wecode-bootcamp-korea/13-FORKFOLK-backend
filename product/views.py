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
        product_list  = []
        category_list = []
        category_name = request.GET.get("category",None)

        if request.GET.get("page"):
            page_num = int(request.GET.get("page"))

        if category_name == "All":
            products      = Product.objects.all()

            for product in products:
                product_id = product.id
                name       = product.name
                price      = product.price
                category   = ShopCategory.objects.get(id=product.category_id)

                product_dic             = {}
                product_dic["id"]       = product_id
                product_dic["name"]     = name
                product_dic["category"] = category.name
                product_dic["price"]    = price

                product_list.append(product_dic)
            page      = page_num
            page_size = 12
            limit     = page * page_size
            offset    = limit - page_size
            return JsonResponse({"page_products":product_list[offset:limit]}, status=201)



        else:
            category_id   = ShopCategory.objects.get(name=category_name)
            products = Product.objects.filter(category_id=category_id)

            for product in products:
                product_id = product.id
                name       = product.name
                price      = product.price
                category   = ShopCategory.objects.get(id=product.category_id)

                product_dic             = {}
                product_dic["id"]       = product_id
                product_dic["name"]     = name
                product_dic["category"] = category.name
                product_dic["price"]    = price

                product_list.append(product_dic)

            return JsonResponse({"category_products":product_list},status=201)
