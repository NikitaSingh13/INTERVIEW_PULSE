"""
URL configuration for interview_pulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from interviews.models import Interview
from datetime import date

def home(request):
    """Home page view"""
    context = {}
    if request.user.is_authenticated:
        interviews = Interview.objects.filter(user=request.user)
        context['total_interviews'] = interviews.count()
        context['upcoming_interviews'] = interviews.filter(date__gte=date.today()).count()
        context['companies_count'] = interviews.values('company').distinct().count()
    return render(request, 'home.html', context)

urlpatterns = [
    path('', home, name='home'),
    path('interviews/', include('interviews.urls')),
    path('preparation/', include('preparation.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
