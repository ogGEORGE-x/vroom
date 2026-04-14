from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html') 
def car(request):
    return render(request, 'car.html')
def cardetails(request):
    return render(request, 'car-details.html')  
def blog(request):
    return render(request, 'blog.html')
def blogdetails(request):
    return render(request, 'blog-details.html')