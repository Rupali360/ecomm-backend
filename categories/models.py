from django.db import models

# Create your models here.

class Categories(models.Model):
    category_name=models.CharField(max_length=255)
    category_img=models.CharField(max_length=255)
    category_details=models.CharField(max_length=255)
