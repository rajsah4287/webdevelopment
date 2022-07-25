from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/first.html")

def  contact(request):
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")