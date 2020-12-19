from django.db import models
import random

def random_number():
    return int(random.randint(1000,9999))

class Courses(models.Model):
    course_name = models.CharField(max_length=100, null=True)
    duration_hours = models.IntegerField(null=True)
    course_price = models.IntegerField(null=True)
    unique_number = models.IntegerField(default = random_number)


