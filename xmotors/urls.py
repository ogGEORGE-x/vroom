from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('car/', views.car, name='car'),
    path('car-details/', views.cardetails, name='car-details'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogdetails, name='blog-details'),
]