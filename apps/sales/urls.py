from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet
router = DefaultRouter()
router.register(r'', SaleViewSet)

urlpatterns = [
    path('sales-page', views.sale_list, name='sales_list'),
    path('', include(router.urls)),
]