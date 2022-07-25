import imp
from itertools import product
import re
from django.shortcuts import render,redirect

from dashboard.forms import StaffForm
from dashboard.models import Staff
from product.models import Product
from order.models import OrderConfirmed

# Create your views here.
def login(request):
    return render(request,"dashboard/adminlogin.html")

def register(request):
    return render(request,"dashboard/register.html")

def save(request):
    form=StaffForm(request.POST)
    form.save()
    return redirect("/dashboard/adminlogin")

def logindo(request):
    email = request.POST.get('username')

    pasw = request.POST.get('password')

    customer = Staff.get_customer_by_email(email)

    if customer:

        if(pasw == customer.password):

               

            print("user exist")

           

            return redirect("/dashboard/admindash")




        else:

               

            return redirect("/dashboard/adminlogin")
    else:
        return redirect("/dashboard/adminlogin")

def show(request):
    return render(request,"dashboard/content.html")

def allproduct(request):
    detail={}
    detail['product'] = Product.objects.all()
    return render(request,"dashboard/allproduct.html",detail)

def orders(request):
    detail={}
    detail['orders']=OrderConfirmed.objects.all()
    return render(request,"dashboard/orders.html",detail)
