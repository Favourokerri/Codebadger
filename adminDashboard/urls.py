from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='dashBoardHome'),
    path('registerStudent', views.registerStudent, name='registerStudent'),
]
