from django.contrib import admin
from django.urls import path, include
from home import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('clients/', include('apps.clients.urls')),
    path('products/', include('apps.products.urls')),
    path('sales/', include('apps.sales.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/products/', include('apps.products.urls')),
    path('api/clients/', include('apps.clients.urls')),
    path('api/sales/', include('apps.sales.urls')),

]
