from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet
router = DefaultRouter()
router.register(r'', ClientViewSet)

urlpatterns = [
    path('clients-page', views.client_list, name='clients_list'),
    path('', include(router.urls)),
]