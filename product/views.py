import json
import random

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
        try:
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
                    product_dic["image"]    = ProductImage.objects.filter(product_id=product_id).values('image_url')[0].get("image_url")

                    product_list.append(product_dic)
                random.shuffle(product_list)
                page      = page_num
                page_size = 12
                limit     = page * page_size
                offset    = limit - page_size
                page_list = product_list[offset:limit]

                if not page_list:
                    return JsonResponse({"massage":"PAGE_ERROR"}, status=409)

                return JsonResponse({"page_products":page_list}, status=201)

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
                    product_dic["image"]    = ProductImage.objects.filter(product_id=product_id).values('image_url')[0].get("image_url")

                    product_list.append(product_dic)

                return JsonResponse({"category_products":product_list},status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)
        except:
            return JsonResponse({'message':'PAGE_ERROR'},status=409)

class ShopDetailView(View):
    def get(self,request,product_id):
        try:
            product = Product.objects.get(id=product_id)
            related_from = product.category_id
            related_to = Product.objects.filter(category_id=related_from)
            image = ProductImage.objects.filter(product_id=product.id).values("image_url")[0].get("image_url") 
            related_list = []
            detail_product   = {
                "id"          : product.id,
                "name"        : product.name,
                "price"       : product.price,
                "description" : product.description,
                "shipping"    : product.shipping,
                "image"       : 
                [image for image in ProductImage.objects.filter(product_id=product.id).values('image_url')]
            }

            for product in related_to:
                related_product            = {}
                related_product["id"]      = product.id
                related_product["name"]    = product.name
                related_product["image"]   = image
                related_product["categoy"] = ShopCategory.objects.get(id=product.category_id).name
                related_product["price"]   = product.price

                related_list.append(related_product)

            random_list = random.sample(related_list,6)
            
            return JsonResponse({'product_info':detail_product,'related_product':random_list},status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)
        except:
            return JsonResponse({'message':'PAGE_ERROR'},status=409)
