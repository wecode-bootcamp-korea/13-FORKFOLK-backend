from django.db import models

class Order(models.Model):
    address      = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)
    user_name    = models.CharField(max_length=50)
    user         = models.ForeignKey('user.User',on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    status       = models.ForeignKey('OrderStatus',on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_status'



