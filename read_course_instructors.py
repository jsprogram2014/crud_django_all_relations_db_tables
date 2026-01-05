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

# Get courses taught by Instructor Yan, via both forward (explicit) and backward (implicit) access
# print(Course.objects.get(instructors__first_name='Yan'))
# print(Instructor.objects.get(first_name='Yan').course_set.all())

# # Get the instructors of Cloud app dev course
# print(Course.objects.get(name__contains='Cloud').instructors.all())

# Check the occupations of the courses taught by instructor Yan
courses_yan=Course.objects.filter(instructors__first_name='Yan')

for coursed in courses_yan:
    learned = coursed.learners.all()
    for learner in learned:
        print(learner.occupation)
