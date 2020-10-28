from django.urls import path, include

urlpatterns = [
    path("my-account",include("user.urls")),
    path("products",include("product.urls")),
    path("order",include("order.urls")),
    path("checkout",include("checkout.urls"))
]
