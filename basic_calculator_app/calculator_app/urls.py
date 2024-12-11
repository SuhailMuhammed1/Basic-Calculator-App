from django.urls import path
from calculator_app import views

urlpatterns = [
    path('', views.homepage),
    path('calculate/', views.calculate),
]