# myapp/urls.py

from django.urls import path
from . import views
# from .views import  home


# function based url pattern 
urlpatterns = [
    path('', views.home),  # Home page view
]


# class based url pattern
# urlpatterns = [
#     path('about/', About.as_view(), name='about'),
#     path('', Home.as_view(), name='home'),
# ]
