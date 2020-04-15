from django.contrib import admin
from django.urls import path
from indian_state import views
urlpatterns = [
    
    path('', views.home , name='Home Page')
]