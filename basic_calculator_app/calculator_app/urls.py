from django.urls import path
from calculator_app import views

urlpatterns = [  # page urls
    path('', views.homepage),
    path('calculate/', views.calculate),
]