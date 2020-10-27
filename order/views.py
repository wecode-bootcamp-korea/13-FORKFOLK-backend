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
        user = request.user
        #print(user)
        #Order.objects.create(user_id=user.id, status_id =OrderStatus.objects.get(status="Before Order").id)
        data = json.loads(request.body)
        product = Product.objects.get(id=data["product_id"])
        order   = Order.objects.get(user_id=user.id)
        product_id = data["product_id"]
        quantity   = data["quantity"]
        price      = product.price
        image      = ProductImage.objects.filter(product_id=118)[0].image_url
        #Cart.objects.create(quantity=quantity,product_id=product_id,order_id=order.id)
        print(1)

        


