from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Interview
from django.contrib.auth.models import User

#temporrary
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def interviews_list(request):
    interview = Interview.objects.all()
    data = list(interview.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_interview(request):
    if request.method == 'POST':
        user = User.objects.get(username= "Russian") # for now hardcoded because we don't have authentication
        company = request.POST.get('company')
        role = request.POST.get('role')
        date = request.POST.get('date')

        interview = Interview.objects.create(user = user, company = company, role = role, date = date)

        return JsonResponse({
            'msg':"you ",
            'compnay':company,
            'role':role,
            'date':date
            })
    
    return JsonResponse({
        'msg':"you are cooked BITCH"
    })


    

