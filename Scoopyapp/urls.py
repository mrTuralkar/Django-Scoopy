# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # Home page view
]
