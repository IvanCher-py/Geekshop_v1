from django.shortcuts import render


def main(request):
    content = {
        'title': 'SupShop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'SupShop - Категории',
        'products': [
            {'foto': '/static/vendor/img/products/Adidas-hoodie.png', 'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.', 'info': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'foto': '/static/vendor/img/products/Blue-jacket-The-North-Face.png', 'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.', 'info': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'foto': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.', 'info': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'foto': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png', 'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.', 'info': 'Плотная ткань. Легкий материал.'},
            {'foto': '/static/vendor/img/products/Black-Dr-Martens-shoes.png', 'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.', 'info': 'Гладкий кожаный верх. Натуральный материал.'},
            {'foto': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.', 'info': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')

# Create your views here.
