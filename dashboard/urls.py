from django.urls import path
from dashboard import views

urlpatterns = [

    path("adminlogin",views.login),
    path("adminregister",views.register),
    path("registerdo",views.save),
    path("logindo",views.logindo),
    path("admindash",views.show),
    path("allproduct",views.allproduct),
    path("orders",views.orders),

   

    
]