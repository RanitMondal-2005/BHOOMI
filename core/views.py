# core/views.py
from django.shortcuts import render

# Landing page (before login) - it has the project intro and the search crop option
def landing_page(request):
    return render(request, 'core/dashboard.html')

# About us
def about_us(request):
    return render(request, 'core/aboutus.html')
