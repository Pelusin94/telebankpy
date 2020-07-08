from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('login/', views.login_page),
    path('logout/', views.logout_page),
]