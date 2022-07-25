
from itertools import product
from math import prod
from django.shortcuts import redirect, render
from customer.models import Customer

from product.forms import ProductForm
from product.models import Product

# Create your views here.
def show(request):
    # product = Product.objects.all()
    data={}
    data['product']= Product.objects.all()
    data['email']= request.session.get('email')
    data['customerId']=request.session.get('customerId')
    return render(request,"product/product.html",data)

def addproduct(request):
    return render(request,"product/add.html")


def saveproduct(request):
    product = ProductForm(request.POST,request.FILES)
    product.save()
    return redirect("/dashboard/allproduct")

def delete(request,id):
    product = Product.objects.get(productid=id)
    product.delete()
    return redirect("/dashboard/allproduct")

def editproduct(request,id):
    data=Product.objects.get(productid=id)
   
    return render(request,"product/editproduct.html",{'data':data})

def updateproduct(request,id):
    data=Product.objects.get(productid=id)
    form=ProductForm(request.POST,request.FILES,instance=data)
    form.save()

    return redirect("/dashboard/allproduct")


def detail(request,id):
    data={}
    data['product']=Product.objects.get(productid = id)
    data['email'] = request.session.get('email')
    data['customerId']= request.session.get('customerId')


    return render(request,"product/detail.html",data)