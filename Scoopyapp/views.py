
# Function based view
# from django.shortcuts import render, HttpResponse

# Create your views here.

# def about(request):
#     # This function returns an HTTP response with the message "Page is not connected"
#     return HttpResponse("Function about page")

# def home(request):
#     # This function renders the 'index.html' template when the home page is accessed
#     return render(request, 'index.html')




# Class based view
from django.http import HttpResponse  # Importing the HttpResponse class from django.http module
from django.views import View  # Importing the View class from django.views module
from django.views.generic import TemplateView  # Importing the TemplateView class from django.views.generic module

class About(View):  # Creating a class About that inherits from the View class
    def get(self, request):  # Defining a method get that takes a request parameter
        return HttpResponse(" Class about page")  #Returning an HttpResponse with the message
                                                      #"Page is not connected"

class Home(TemplateView):  # Creating a class Home that inherits from the TemplateView class
    template_name = 'index.html'  # Setting the template_name attribute to 'index.html'


