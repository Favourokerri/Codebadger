"""
    this file contains all views related to courses
"""
from django.shortcuts import  render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse
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

@decorators.adminOnly
def search_suggestions(request):
    query = request.GET.get('q')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if query:
            results = Course.objects.filter(name__icontains=query)
            data = list(results.values('id', 'name'))
            return JsonResponse({'result': data})
        else:
            return JsonResponse({'error': 'please enter a search parameter'})
    
    else:
        if query:
            results = Course.objects.filter(name__icontains=query)
        else:
            messages.warning(request, "please enter a search parameter")
            return redirect("courses")
    return render(request, 'admin/courses.html', {'courses': results})

def single_course(request, id):
    try:
        course = get_object_or_404(Course, id=id)
        print(course)
        context = {"course": course}

    except Exception as e:
        messages.error(request, 'some error occured')
        return redirect('course')

    return render(request, 'admin/singleCourse.html', context)