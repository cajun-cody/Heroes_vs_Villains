from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_types_list), #From views.py execute product_list function
    path('<int:pk>/', views.single_super_type) #Passes the pk as an integer through the path.
]