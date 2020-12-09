from django.shortcuts import render


def main(request):
    content = {
        'title': 'SupShop'
    }
    return render(request, 'mainapp/index.html', content)




def products(request):
    content = {
        'title': 'SupShop - Категории'
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')

# Create your views here.
