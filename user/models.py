from django.db      import models

#from product.models import Product

# Create your models here.

class User(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
   
    class Meta:
        db_table = 'users'

class Order(models.Model):
    address        = models.CharField(max_length=300)
    phone_number   = models.CharField(max_length=50)
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    status         = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    #product        = models.ManyToManyField('product.Product', through='product.Cart')
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_status'
