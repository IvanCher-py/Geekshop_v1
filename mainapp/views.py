from django.shortcuts import render
from mainapp.models import ProductCategory, Product

def main(request):
    content = {
        'title': 'SupShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'SupShop - Категории',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def clothes(request):
    contex = {
        'title': 'SupShop - Категории',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/clothes.html', context=contex)



# Create your views here.
