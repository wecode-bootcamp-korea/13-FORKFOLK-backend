from django.db   import models

#from user.models import User,Order

# Create your models here.

class ShopCategory(models.Model):
    name  = models.CharField(max_length=50)

    class Meta:
        db_table = 'shop_categories'

class Product(models.Model):
    category         = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    name             = models.CharField(max_length=50)
    price            = models.DecimalField(default=0, max_digits=5, decimal_places=2) 
    description      = models.TextField()
    shipping         = models.TextField()
    orders           = models.ManyToManyField('order.Order', through='Cart', related_name='orders')
    related_products = models.ManyToManyField('self', through='RelatedProduct', symmetrical=False)

    class Meta:
        db_table = 'products'

class RelatedProduct(models.Model):
    from_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='to_product')
    to_product   = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='from_product')

    class Meta:
        db_table = 'related_products'

class ProductImage(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=300)
    
    class Meta:
        db_table = 'product_images'

class Cart(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    order    = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'


