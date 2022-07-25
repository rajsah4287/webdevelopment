from django.urls import path
from product import views

urlpatterns = [

    path("productpage",views.show),
    path("addproduct",views.addproduct),
    path("save",views.saveproduct),
    path("deleteproduct/<int:id>",views.delete),
    path("editproduct/<int:id>",views.editproduct),
    path("updateproduct/<int:id>",views.updateproduct),
    path("detail/<int:id>",views.detail),
   

    
]