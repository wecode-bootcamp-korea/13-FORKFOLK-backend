from django.urls    import path

from checkout.views import CheckOutView

urlpatterns = [
    path("",CheckOutView.as_view())
]
