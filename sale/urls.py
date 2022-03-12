
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('saleapp.urls')),
    path('admin/', admin.site.urls),
]
