from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import mainapp.views as mainapp


urlpatterns = [
    path('', mainapp.main, name='index'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contact, name='contact'),
    path('clothes/', mainapp.contact, name='clothes'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)