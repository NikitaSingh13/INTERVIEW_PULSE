from django.urls import path
from . import views

urlpatterns = [
    path('', views.preparation, name = 'preparation')
]
