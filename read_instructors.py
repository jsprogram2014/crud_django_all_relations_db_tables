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

# print(Instructor.objects.get(first_name='Yan'))
# print(Instructor.objects.get(first_name='Andy'))
# print(Instructor.objects.filter(full_time= False))
print(Instructor.objects.filter(first_name__istartswith='J', total_learners__gt=30000))
# print(Instructor.objects.all())