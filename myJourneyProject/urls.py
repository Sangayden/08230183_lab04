"""
URL configuration for myJourneyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# DJANGO LABWORK/myJourneyProject/myJourneyProject/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # 1. THIS LINE INCLUDES THE BUILT-IN ADMIN INTERFACE URLS
    path('admin/', admin.site.urls), 
    
    # 2. This line links your app's pages (home, aboutme)
    # Ensure this module path is correct: 'SCJourney.urls'
    path('', include('SCJourney.urls')), 
]