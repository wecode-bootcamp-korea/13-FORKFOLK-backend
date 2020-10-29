from django.urls import path

from order.views import OrderView

urlpatterns = [
    path("",OrderView.as_view())
]
