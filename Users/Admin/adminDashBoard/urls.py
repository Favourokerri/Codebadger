from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='adminDashBoard'),
    path('registerStudent', views.registerStudent, name='registerStudent'),
]
