from django.db import models

# Create your models here.

class Staff(models.Model):
    staffid=models.AutoField(auto_created=True,primary_key=True)
    email=models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        db_table="Staff"

    @staticmethod

    def get_customer_by_email(email):

        try:

            return Staff.objects.get(email = email)

        except:

            return False