from django.db import models

# Create your models here.


# Create your models here.
class Product(models.Model):
    productid=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=100)
    brand = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)
    image = models.FileField(upload_to="static/images/product",default="default.jpg")
   

    class Meta:
        db_table="Product"