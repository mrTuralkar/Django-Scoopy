"""
URL configuration for Scoopy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Scoopyapp import views


# function based url pattern
# urlpatterns = [
#     path('admin/', admin.site.urls),  # URL pattern for the Django admin interface
#     path('about/', views.about,name="about"),  # URL pattern for the 'about' page handled by the 'about' view
#     path('', include('Scoopyapp.urls')),  # Includes URL patterns from the 'Scoopyapp' application

# ]



# # class based url pattern
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the Django admin interface
    path('about/', views.About.as_view(), name="about"),
    path('', include('Scoopyapp.urls')),  # Includes URL patterns from the 'Scoopyapp' application
]







