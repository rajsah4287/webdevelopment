from django.shortcuts import redirect, render

from customer.forms import CustomerForm
from customer.models import Customer

# Create your views here.
def login(request):
    return render(request,"customer/login.html")

def register(request):
    return render(request,"customer/register.html")


def save(request):
    form=CustomerForm(request.POST)
    form.save()
    return redirect("/customer/login")

def log(request):
    email = request.POST.get('username')

    pasw = request.POST.get('password')

    customer = Customer.get_customer_by_email(email)

    if customer:

        if(pasw == customer.password):
            request.session['email'] = customer.email
            request.session['customerId'] = customer.customerid

               

            print("user exist")

           

            return redirect("/product/productpage")




        else:

               

            return redirect("/customer/login")
    else:
        return redirect("/customer/login")
           

        

