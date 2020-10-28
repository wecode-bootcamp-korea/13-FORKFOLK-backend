import json
import random

from django.db.models          import Q
from django.views              import View
from django.views.generic.list import ListView

from django.http  import (
                        JsonResponse,
                        HttpResponse
                        )
from user.utils   import user_validator
from order.models import (
                        Order,
                        OrderStatus
                        )
from product.models import (
                        Cart,
                        Product,
                        ProductImage
                        )
class OrderView(View):
    @user_validator
    def post(self,request):
        data     = json.loads(request.body)
        product  = Product.objects.get(id=data["product_id"])
        user     = request.user
        quantity = data['quantity']
        status   = OrderStatus.objects.get(status = data["status"])
        try:
            order = Order.objects.get(user_id=user.id, status_id=status.id)
            Cart.objects.create(product_id=product.id, order_id=order.id, quantity=quantity)
            return JsonResponse({"message":"SUCCESS!"}, status=201)

        except Order.DoesNotExist:
            order = Order.objects.create(user_id=user.id, status_id=status.id)
            Cart.objects.create(product_id=product.id, order_id=order.id, quantity=quantity)
            return JsonResponse({"message":"SUCCESS!"}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)

    @user_validator
    def get(self,request):
        try:
            data      = json.loads(request.body)
            status    = OrderStatus.objects.get(status = data["status"])
            user      = request.user
            order_id  = Order.objects.get(user_id=user.id, status=status.id).id
            cart_list = Cart.objects.filter(order_id=order_id).values()

            product_list = [{
                "id"       : cart["product_id"],
                "quantity" : cart["quantity"],
                "name"     : Product.objects.get(id=cart["product_id"]).name,# id=id로 테스트 해보기
                "image"    : ProductImage.objects.filter(product_id=cart["product_id"]).values('image_url')[0].get("image_url"),
                "price"    : Product.objects.get(id=cart["product_id"]).price
            } for cart in cart_list]

            return JsonResponse({"in cart list":product_list},status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)

    @user_validator
    def delete(self,request):
        try:
            data      = json.loads(request.body)
            status    = OrderStatus.objects.get(status = data["status"])
            user      = request.user
            order_id  = Order.objects.get(user_id=user.id, status=status.id).id
            cart_list = Cart.objects.filter(order_id=order_id).values()

            del_product = Product.objects.get(id=data["product_id"])
            in_cart = Cart.objects.get(product_id=del_product)
            in_cart.delete()

            product_list = [{
                "id"       : cart["product_id"],
                "quantity" : cart["quantity"],
                "name"     : Product.objects.get(id=cart["product_id"]).name,# id=id로 테스트 해보기
                "image"    : ProductImage.objects.filter(product_id=cart["product_id"]).values('image_url')[0].get("image_url"),
                "price"    : Product.objects.get(id=cart["product_id"]).price
            } for cart in cart_list]

            return JsonResponse({"remain list":Product_list}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)
        except:
            return JsonResponse({"message":"delete failed"}, status=400)
