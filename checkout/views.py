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

#class CheckOutView(View):
#    @user_validator
#    def get(self,request):
#        try:
           # data = json.loads(request.body)
           # user_id  = request.user.id
           # print(user_id)
           # cart     = Order.objects.filter(user_id=8, status=1).prefetch_related("cart_set")
        #print(cart)
        #except:
            #print("get error!")




#    @user_validator
#    def post(self,request):
#        try:
#            user = request.user
#            data = json.loads(request.body)
#            address = data["address"]
#            phone_number = data["phone_number"]
#            user_name = data["name"]
#            order_id = Order.objects.get(user_id=user.id).id

            

#        except:
#            print("error!")

