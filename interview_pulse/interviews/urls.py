from django.urls import path
from . import views

urlpatterns = [
    path('list', views.interviews_list, name='interviews_list'),
    path('add', views.add_interview, name='add_interview'),
    path('get_interview/<str:username>', views.get_interview, name='get_interview'),
]
