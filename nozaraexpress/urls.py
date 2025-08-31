
from django.contrib import admin
from django.urls import path, include
import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
   
]





