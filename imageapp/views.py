from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


def home(request):
    cats=Category.objects.all()
    images=Image.objects.all()   #datebase se sari pics ko images me daal dega
    data={'images':images, 'cats':cats }    #fir wo images ki values 'data' me jayegi

    return render(request, 'home.html',data)   # "data"  fir home .html me chala jayega
    #return HttpResponse("this is home")

def categorys(request,cid):
    cats = Category.objects.all()

    categorys = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=categorys)  # datebase se sari pics ko images me daal dega
    data = {'images': images, 'cats': cats}
    return render(request, 'home.html', data)

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
 #   return HttpResponse("this is contact home")

def aboutus(request):
    return render(request, 'about.html')  #render  about.html page pe transfer kr dega
    #return HttpResponse("this is about page")
