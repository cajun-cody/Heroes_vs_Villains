from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_types_list), 
    path('<int:pk>/', views.single_super_type) 
    
    ]