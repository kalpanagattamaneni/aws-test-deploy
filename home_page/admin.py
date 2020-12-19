from django.contrib import admin

from .models import Courses

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'duration_hours', 'course_price', 'unique_number']