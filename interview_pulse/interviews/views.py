import json
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Interview
from django.contrib.auth.models import User

#temporrary
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

'''
Get all interviews list
'''
def interviews_list(request):
    interview = Interview.objects.all()
    data = list(interview.values())
    return JsonResponse(data, safe=False)

'''
get interview list by username
'''

def get_interview(request, username):
    try:
        user = User.objects.get(username = username)
        interviews = Interview.objects.filter(user = user)
        data = list(interviews.values())
        return JsonResponse(data, safe = False)

    except:
        return JsonResponse({'msg': 'something is wrong with your get id'})
    
'''
add new interview to the list 
'''

@csrf_exempt
def add_interview(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            company = data.get('company')
            role = data.get('role')
            interview_date = data.get('date')
        except:
            username = request.POST.get('username')
            company = request.POST.get('company')
            role = request.POST.get('role')
            interview_date = request.POST.get('date')

        if not username or not company or not role or not interview_date:
            messages.error(request, 'Missing required fields')
            return render(request, 'interviews/add_interview.html', {'today': date.today()})
        
        try:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.save()
        except:
            messages.error(request, 'Error with user')
            return render(request, 'interviews/add_interview.html', {'today': date.today()})
        
        try:
            interview = Interview.objects.create(user=user, company=company, role=role, date=interview_date)
            messages.success(request, f'Interview with {company} added successfully!')
            return redirect('/interviews/list')
        except Exception as e:
            messages.error(request, f'Error creating interview: {str(e)}')
            return render(request, 'interviews/add_interview.html', {'today': date.today()})
    
    # GET request - show the form
    return render(request, 'interviews/add_interview.html', {'today': date.today()})


    

