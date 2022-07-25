
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("home.urls")),
    path("customer/",include("customer.urls")),
    path("product/",include("product.urls")),
    path("dashboard/",include("dashboard.urls")),
    path("order/",include("order.urls")),
    
  
   
]
