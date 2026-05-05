from django.shortcuts import render
from .models import Car, Blog, Contact, About, Seller
import json
import logging
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html') 
def car(request):
    return render(request, 'car.html', {'cars': car})
def car2(request):
    return render(request, 'car2.html')
def car3(request):
    return render(request, 'car3.html')
def carfl(request):
    return render(request, 'carfl.html')
def cardetails(request):
    return render(request, 'car-details.html')  
def blog(request):
    return render(request, 'blog.html')
def blogdetails(request):
    return render(request, 'blog-details.html')
def add_car(request):
    if request.method == 'POST':
        # Here you would typically handle the form submission, e.g., save the car details to the database
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        # You can add code here to save the car details to your database
        # For now, we will just render the same page after submission
    return render(request, 'add_car.html')
# def bmw(request):
#     return render(request, 'bmw.html')
def blogs2(request):
    return render(request, 'blogs2.html')
def blogs3(request):
    return render(request, 'blogs3.html')
def blogsfl(request):
    return render(request, 'blogsfl.html')
def checkout(request):
    return render(request, 'checkout.html')
