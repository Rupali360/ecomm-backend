from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=255)
    product_img=models.CharField(max_length=255)
    product_category=models.IntegerField()
    price=models.IntegerField()
    discounted_price=models.IntegerField()
    product_desc=models.CharField(max_length=255)
