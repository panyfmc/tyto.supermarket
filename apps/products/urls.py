from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
router = DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    path('products-page/', views.product_list, name='products_list'),
    path('', include(router.urls)),
]
