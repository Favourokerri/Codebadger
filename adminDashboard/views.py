from django.shortcuts import render

# Create your views here.
def home(request):
    """ view for main dashBoard"""
    return render(request, 'admin/home.html')

def registerStudent(request):
    """ view to register new student"""
    return render(request, 'admin/registerStudent.html')
