from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.adduser),
    path('user/<int:pk>/',views.get_user),
    path('search/',views.search),
    path('search_user/',views.search_user_in_data_base),
    
    
]