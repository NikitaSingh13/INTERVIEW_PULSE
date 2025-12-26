from django.urls import path
from . import views

urlpatterns = [
    path('interviews', views.interviews_list, name = 'interviews'),
    path('add', views.add_interview, name = 'add_interview')
]
