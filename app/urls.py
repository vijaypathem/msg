from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.ViewMessage, name='inbox'),
    path('', views.HomeView, name='home'),
    path('send-message/', views.send_message, name='send_message'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
