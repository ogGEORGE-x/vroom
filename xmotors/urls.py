from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('car/', views.car, name='car'),
    path('car2/', views.car2, name='car2'),
    path('car3/', views.car3, name='car3'),
    path('carfl/', views.carfl, name='carfl'),
    path('car-details/', views.cardetails, name='car-details'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blogdetails, name='blog-details'),
    path('add_car/', views.add_car, name='add_car'),
    path('blogs2/', views.blogs2, name='blogs2'),
    path('blogs3/', views.blogs3, name='blogs3'),
    path('blogsfl/', views.blogsfl, name='blogsfl'),
    path('checkout/', views.checkout, name='checkout'),
    # path('bmw/', views.bmw, name='bmw'),
]  