from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/<str:email>/', views.home, name='home_with_email')
]
