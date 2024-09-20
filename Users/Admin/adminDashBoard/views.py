from django.shortcuts import render
from .decorators import adminOnly
from Users.Admin.CoursesManagement.models import Course

# Create your views here.
@adminOnly
def home(request):
    """ view for main dashBoard"""
    course_count =  courses = Course.objects.all().count()

    context = {'course_count': course_count}
    return render(request, 'admin/home.html', context)

@adminOnly
def registerStudent(request):
    """ view to register new student"""
    courses = Course.objects.all()

    context = {'courses':courses}
    return render(request, 'admin/registerStudent.html', context)