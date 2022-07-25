
from django.db import models

# Create your models here.
class Customer(models.Model):
    customerid=models.AutoField(auto_created=True,primary_key=True)
    customerName=models.CharField(max_length=255)
    email=models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table="Customer"

    @staticmethod

    def get_customer_by_email(email):

        try:

            return Customer.objects.get(email = email)

        except:

            return False