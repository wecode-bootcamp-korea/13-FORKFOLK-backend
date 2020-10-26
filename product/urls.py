from django.urls   import path

from product.views import ShopAllView 

urlpatterns = [
    path('',ShopAllView.as_view())
    ]
