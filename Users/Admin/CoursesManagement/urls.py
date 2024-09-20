from django.urls import path
from . import views

urlpatterns = [
    path('createCourse/', views.create_course, name='create_course'),
    path('courses/', views.courses, name='courses'),
    path('publishedCourse', views.published_course, name='published_course'),
    path('draftCourse', views.draft_course, name='draft_course'),
]