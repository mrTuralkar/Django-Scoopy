# myapp/urls.py

from django.urls import path
from . import views

# class based url pattern
# from .views import  About,Home

# urlpatterns = [
#     path('about/', About.as_view(), name='about'),
#     path('', Home.as_view(), name='home'),
# ]

# function based url pattern 
urlpatterns = [
    path('', views.home),  # URL pattern for the home page, handled by the 'home' view
]


