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
            page = request.GET.get("page")
            category_name = request.GET.get("category")

            if page and category_name:
                page = int(page)
                if category_name == "All":
                    products = Product.objects.all()
                else:
                    category_id = ShopCategory.objects.get(name=category_name).id
                    products    = Product.objects.filter(category_id=category_id)

                product_list = [{
                    "id"       : product.id,
                    "name"     : product.name,
                    "category" : ShopCategory.objects.get(id=product.category_id).name,
                    "price"    : product.price,
                    "image"    : ProductImage.objects.filter(product_id=product.id).values('image_url')[0].get("image_url")} for product in products]


                random.shuffle(product_list)
                page_size = 12
                limit     = page * page_size
                offset    = limit - page_size
                page_list = product_list[offset:limit]

                if not page_list:
                    return JsonResponse({"massage":"PAGE_ERROR"}, status=409)

                return JsonResponse({"page_products":page_list}, status=201)
            else:
                return JsonResponse({"message":"Not Found URL"},status=400)
#            category_list = []
#            category_name = request.GET.get("category",None)
#
#            if request.GET.get("page"):
#                page_num = int(request.GET.get("page"))
#
#            if category_name == "All":
#                products = Product.objects.all()
#
#                product_list = [{
#                    "id"       : product.id,
#                    "name"     : product.name,
#                    "category" : ShopCategory.objects.get(id=product.category_id).name,
#                    "price"    : product.price,
#                    "image"    : ProductImage.objects.filter(product_id=product.id).values('image_url')[0].get("image_url")} for product in products]
#
#                random.shuffle(product_list)
#                page      = page_num
#                page_size = 12
#                limit     = page * page_size
#                offset    = limit - page_size
#                page_list = product_list[offset:limit]
#
#                if not page_list:
#                    return JsonResponse({"massage":"PAGE_ERROR"}, status=409)
#
#                return JsonResponse({"page_products":page_list}, status=201)
#
#            else:
#                category_id   = ShopCategory.objects.get(name=category_name)
#                products = Product.objects.filter(category_id=category_id)
#                product_list = [{
#                    "id"       : product.id,
#                    "name"     : product.name,
#                    "category" : ShopCategory.objects.get(id=product.category_id).name,
#                    "price"    : product.price,
#                    "image"    : ProductImage.objects.filter(product_id=product.id).values('image_url')[0].get("image_url")} for product in products]
#
#                return JsonResponse({"category_products":product_list},status=201)
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
            images = [image for image in ProductImage.objects.filter(product_id=product.id).values('image_url')]
            image_list = [image["image_url"] for image in images] 

            detail_product   = {
                "id"           : product.id,
                "name"         : product.name,
                "price"        : product.price,
                "descriptions" : {
                    "description" : product.description,
                    "shipping"    : product.shipping
                },
                "shipping"     : product.shipping,
                "image"        : image_list
            }

            related_list = [({
                "id"       : product.id,
                "name"     : product.name,
                "image"    : image,
                "category" : ShopCategory.objects.get(id=product.category_id).name,
                "price"    : product.price}) for product in related_to]

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
