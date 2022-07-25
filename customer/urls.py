from django.urls import path
from customer import views

urlpatterns = [

    path("login",views.login),
    path("register",views.register),
    path("save",views.save),
    path("log",views.log),

    
]