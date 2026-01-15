from django.urls import path
from . import views

urlpatterns = [
    path('', views.preparation_home, name='preparation_home'),
]
