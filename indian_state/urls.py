from django.contrib import admin
from django.urls import path,include
from indian_state import views
urlpatterns = [
    
    path('', views.home , name='Home Page'),
    path('login', views.login , name='login'),
    path('accounts/',include('allauth.urls'))
    
]