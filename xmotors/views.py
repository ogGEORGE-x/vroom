from django.shortcuts import render
from .models import Car, Blog, Contact, About, Seller

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html') 
def car(request):
    cars= Car.objects.all() 
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    body_style = request.GET.get('body_style')
    condition = request.GET.get('condition')
    transmission = request.GET.get('transmission')
    color = request.GET.get('color')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if brand:
        cars = cars.filter(brand__iexact=brand)
    if model:
        cars = cars.filter(model__iexact=model)
    if body_style:
        cars = cars.filter(body_style__iexact=body_style)
    if condition:
        cars = cars.filter(condition__iexact=condition)
    if transmission:
        cars = cars.filter(transmission__iexact=transmission)
    if color:
        cars = cars.filter(color__iexact=color)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:        cars = cars.filter(price__lte=max_price)
    return render(request, 'car.html', {
        'cars': cars,
        'brands': Car.objects.values_list('brand', flat=True).distinct(),
        'models': Car.objects.values_list('model', flat=True).distinct(),
        'body_styles': Car.objects.values_list('body_style', flat=True).distinct(),
        'conditions': Car.objects.values_list('condition', flat=True).distinct(),
        'transmissions': Car.objects.values_list('transmission', flat=True).distinct(),
        'colors': Car.objects.values_list('color', flat=True).distinct(),
        'min_price': min_price,
        'max_price': max_price,
        })
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