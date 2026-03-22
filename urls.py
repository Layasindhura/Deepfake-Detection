"""project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, register, index, predict_page,cuda_full, main, login, logout_view, image_detection

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    path('', main, name='main'),
    path('index/', index, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('login', login, name='login'),
    path('predict/', predict_page, name='predict'),
    path('image-detection/', views.image_detection, name='image_detection'),
    path('cuda_full/',cuda_full,name='cuda_full'),
    path('logout/', logout_view, name='logout'),
]
