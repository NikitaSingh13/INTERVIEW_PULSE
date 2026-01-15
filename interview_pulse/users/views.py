from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from interviews.models import Interview
from datetime import date

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'users/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'users/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'users/register.html')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('/users/login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'users/register.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('/')

@login_required
def profile(request):
    user = request.user
    interviews = Interview.objects.filter(user=user)
    total_interviews = interviews.count()
    upcoming_interviews = interviews.filter(date__gte=date.today()).count()
    companies = interviews.values('company').distinct()
    companies_count = companies.count()
    recent_interviews = interviews.order_by('-date')[:5]
    
    context = {
        'total_interviews': total_interviews,
        'upcoming_interviews': upcoming_interviews,
        'companies_count': companies_count,
        'recent_interviews': recent_interviews,
    }
    
    return render(request, 'users/profile.html', context)
