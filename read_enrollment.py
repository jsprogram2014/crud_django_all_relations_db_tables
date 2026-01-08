# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date

from crud.models import Instructor
# Your code starts from here:

# Get the user information about learner David
print(Learner.objects.get(first_name='David').user_ptr)

# Get learner David information from user
print(User.objects.get(first_name='David').learner)

# Get all learners for Introduction to Python course
print(Course.objects.get(name='Introduction to Python').learners.all())

# Check the occupation list for the courses taught by instructor Yan
instructor_yan_courses=Course.objects.filter(instructors__first_name='Yan')

for course in instructor_yan_courses:
    learners=course.learners.all()

    for learner in learners:
        print(learner.occupation)

# Check which courses the developer learners are enrolled in Aug, 2020
filtered_courses=Enrollment.objects.filter(learner__occupation='developer',date_enrolled__month=8, date_enrolled__year=2020)

for coursed in filtered_courses:
    print(coursed.course.name)