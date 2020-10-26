import os
import django
import csv
import sys
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','kinfolk.settings')
django.setup()

from product.models import ShopCategory,Product,RelatedProduct,ProductImage,Cart

CSV_PATH_PRODUCTS = '../kinfolk-file/category/product-total.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader,None)
    for row in data_reader:
        if row[0]:
            category_name = row[0]
            ShopCategory.objects.create(name=category_name)
        product_name = row[2]
        category_id  = ShopCategory.objects.get(name=category_name).id
        description  = row[7]
        shipping     = row[8]
        price        = row[3]
        Product.objects.create(category_id=category_id,name=product_name,description=description,shipping=shipping,price=price)
        images       = row[4:7]
        product_id   = Product.objects.get(name=product_name).id
        for image in images:
            ProductImage.objects.create(product_id=product_id, image_url=image)

        from_product = Product.objects.get(name=product_name)
        to_product   = Product.objects.filter(category_id=category_id)
        for to in to_product:
            RelatedProduct.objects.create(
            from_product_id=from_product.id,
            to_product_id  =to.id
            )


