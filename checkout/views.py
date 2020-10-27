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



# Create your views here.
