from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),  #добавляем маршрут
    path('organelle/<str:organelle_type>/', views.organelle_detail, name='organelle_detail'),
]