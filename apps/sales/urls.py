from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sales_list'),
]