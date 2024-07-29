from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Page is not connected")

def home(request):
    return render(request,'index.html')

