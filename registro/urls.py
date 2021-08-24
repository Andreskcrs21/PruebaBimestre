from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('lista/', views.lista, name='lista')
]
