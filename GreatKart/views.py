from django.http import  HttpResponse
from django.shortcuts import render
from store.models import product
from Subject_Category.models import Subject_Category

def home(request):
    #products = product.objects.all().filter(is_available=True)
    products=Subject_Category.objects.all().filter()
    context={
        'products':products,
    }
    return render(request, 'home.html', context)


def navbar(request):
    categories=Subject_Category.objects.all().filter()
    context={
        'categories':categories,
    }
    return render(request, 'navbar.html', context)