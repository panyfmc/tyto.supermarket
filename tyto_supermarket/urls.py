from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('clients/', include('apps.clients.urls')),
    path('products/', include('apps.products.urls')),
    #path('sales/', include('apps.sales.urls')),

]
