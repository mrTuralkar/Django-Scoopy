# myapp/urls.py

from django.urls import path
from . import views


# # function based url pattern 
# urlpatterns = [
#     path('', views.home, name="home"),  # URL pattern for the home page, handled by the 'home' view
# ]




# class based url pattern
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
