
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.extract_detail),
    path('success/', views.success, name = 'success')
    
]
