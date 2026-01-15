from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def preparation_home(request):
    return render(request, 'preparation/preparation_home.html')
