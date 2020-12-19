from django.shortcuts import render
from django.http import Http404

from .models import Courses, random_number

def course(request):
    course = Courses.objects.all()
    return render(request, 'course.html',{
        'course':course,
        })

def course_detail(request, id):
    try:
        courses = Courses.objects.get(id=id)
    except Courses.DoesNotExist:
        raise Http404('Course not found')
    return render(request, 'course_detail.html',{
        'courses': courses, 
    })


    