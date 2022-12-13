from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_supers), #From views.py execute product_list function
    path('<int:pk>/', views.single_super) #Passes the pk as an integer through the path.
]