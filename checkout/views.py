import json
import random

from django.db.models          import Q
from django.views              import View
from django.views.generic.list import ListView

from django.http  import (
                        JsonResponse,
                        HttpResponse
                        )

from user.utils      import user_validator
from checkout.models import Checkout
from order.models    import (
                        Order,
                        OrderStatus
                        )
from product.models  import (
                        Cart,
                        Product,
                        ProductImage
                        )

class CheckOutView(View):
    @user_validator
    def get(self,request):
        try:
            data      = json.loads(request.body)
            status    = OrderStatus.objects.get(status = data["status"])
            user      = request.user
            order_id  = Order.objects.get(user_id=user.id, status=status.id).id
            cart_list = Cart.objects.filter(order_id=order_id).values()

            checkout_list = [{
                "id"       : cart["product_id"],
                "quantity" : cart["quantity"],
                "name"     : Product.objects.get(id=cart["product_id"]).name,
                "price"    : Product.objects.get(id=cart["product_id"]).price
            } for cart in cart_list]

            return JsonResponse({"checkout list":checkout_list},status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)

    @user_validator
    def post(self,request):
        try:
            user = request.user
            data = json.loads(request.body)
            order_id = Order.objects.get(user_id=user.id).id
            order = Order.objects.get(id=order_id)

            order.address      = data["address"]
            order.phone_number = data["phone_number"]
            order.user_name    = data["name"]

            return JsonResponse({"message":"SUCCESS"},status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=409)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=409)
        except TypeError:
            return JsonResponse({'message':'TYPE_ERROR'},status=409)
