from django.shortcuts import render

# Create your views here.
# scJourney/views.py

from django.shortcuts import render

def index(request):
    """
    Renders the main index page, which describes the learning journey.
    This view links to the 'aboutMe.html' page.
    """
    return render(request, 'SCJourney/index.html')

def aboutMe(request):
    """
    Renders the about me page, providing details about the student.
    This view links back to the 'index.html' page.
    """
    return render(request, 'SCJourney/aboutMe.html')