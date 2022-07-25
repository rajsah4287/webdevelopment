from django.shortcuts import render,redirect
from order.forms import OrderForm

# Create your views here.
def save(request):
    order = OrderForm(request.POST)
    order.save()
    return redirect("/product/productpage")