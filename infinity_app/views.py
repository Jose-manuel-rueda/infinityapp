from django.shortcuts import render

def home(request):
    return render(request, 'infinity_app/home.html')

def about(request):
    return render(request, 'infinity_app/about.html')

def contact(request):
    return render(request, 'infinity_app/contact.html')
