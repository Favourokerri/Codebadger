"""
    this file contains all views related to courses
"""
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.db import IntegrityError
from Users.Admin.adminDashBoard import decorators
from .models import Course

# Create your views here.
@decorators.adminOnly
def create_course(request):
    """ view for creating course"""
    if request.method == 'POST':
        try:
            course_image = request.FILES['course-image']
            name= request.POST['name']
            fee = request.POST['fee']
            about = request.POST['about']
            course = Course.objects.create(course_image=course_image,
                                            name=name,
                                            fee=fee,
                                            about=about,
                                            )
            messages.success(request, 'course created successfully')
            return redirect('create_course')
        except IntegrityError:
            messages.error(request, 'course with this name alredy exist')
            return redirect('create_course')
        except Exception as e:
            print(e)
            messages.error(request, 'error while creating course')
            return redirect('create_course')
    return render(request, 'admin/createCourse.html')

@decorators.adminOnly
def courses(request):
    """ view to see all courses"""
    try:
        courses = Course.objects.all()

        context = {'courses':courses}
    except IntegrityError:
        messages.error(request, 'course with this name alredy exixts')
        return redirect('create_course')
    return render(request, 'admin/courses.html', context)

@decorators.adminOnly
def published_course(request):
    """ view to see published courses"""
    published_courses = Course.objects.filter(status='published')

    context = {'courses': published_courses}
    return render(request, 'admin/courses.html', context)

@decorators.adminOnly
def draft_course(request):
    """ view to courses saved as draft"""
    draft_courses = Course.objects.filter(status='draft')

    context = {'courses': draft_courses}
    return render(request, 'admin/courses.html', context)
