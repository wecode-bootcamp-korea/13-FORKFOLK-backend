from django.db import models

class Checkout(models.Model):
    order        = models.ForeignKey("order.Order", on_delete=models.CASCADE)
    address      = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)
    user_name    = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "checkouts"


