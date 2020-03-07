from django.urls import path
from registro import views


urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    ]
    
