from django.contrib import admin

# Register your models here.
# scJourney/admin.py

from django.contrib import admin
from .models import Milestone

# Register the Milestone model so it appears in the Django Admin interface
admin.site.register(Milestone)