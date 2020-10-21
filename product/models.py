from django.db   import models

#from user.models import User,Order

# Create your models here.

class ShopCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'shop_categories'

class Product(models.Model):
    category    = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    price       = models.IntegerField(default=0)
    description = models.TextField()
    shipping    = models.TextField()
    orders      = models.ManyToManyField('user.Order',through='Cart', related_name='orders')

    class Meta:
        db_table = 'products'

class RelatedProduct(models.Model):
    product         = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_product')

    class Meta:
        db_table = 'related_products'

class ProductImage(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=300)
    
    class Meta:
        db_table = 'product_images'

class Cart(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    order    = models.ForeignKey('user.Order', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'


