from django.urls   import path

from product.views import ShopAllView,ShopDetailView 

urlpatterns = [
    path('',ShopAllView.as_view()),
    path('/<int:product_id>',ShopDetailView.as_view())
    ]
