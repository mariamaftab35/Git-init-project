from django.urls import path
from . import views

urlpatterns = [
    path('w/', views.welcome),
    path('i/', views.index)
]
