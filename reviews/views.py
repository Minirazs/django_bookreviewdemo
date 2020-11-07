from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to reviews")

def index(request):
    return render(request, 'reviews/index.template.html')
