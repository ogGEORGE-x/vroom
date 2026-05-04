"""
URL configuration for vroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('xmotors.urls')),
    path('about/', include('xmotors.urls')),
    path('contact/', include('xmotors.urls')),
    path('car/', include('xmotors.urls')),
    path('car2/', include('xmotors.urls')),
    path('car3/', include('xmotors.urls')),
    path('carfl/', include('xmotors.urls')),
    path('car/car2/', include('xmotors.urls')),
    path('car/car3/', include('xmotors.urls')),
    path('car/carfl/', include('xmotors.urls')),
    path('car/car2/car3/carfl/', include('xmotors.urls')),
    path('car-details/', include('xmotors.urls')),
    path('blog/', include('xmotors.urls')),
    path('blog-details/', include('xmotors.urls')),
    path('add_car/', include('xmotors.urls')),
    path('add_blog/', include('xmotors.urls')),
    path('update_car/<int:car_id>/', include('xmotors.urls')),
    path('delete_car/<int:car_id>/', include('xmotors.urls')),
    path('update_blog/<int:blog_id>/', include('xmotors.urls')),
    path('delete_blog/<int:blog_id>/', include('xmotors.urls')),
    path('search/', include('xmotors.urls')),
    path('filter/', include('xmotors.urls')),
    path('sort/', include('xmotors.urls')),
    path('register/', include('xmotors.urls')),
    path('login/', include('xmotors.urls')),
    path('logout/', include('xmotors.urls')),
    path('profile/', include('xmotors.urls')),
    path('about/cars/', include('xmotors.urls')),
    path('about/cars/cars2/cars3/carfl/', include('xmotors.urls')),
    path('about/cars/cars2/cars3/', include('xmotors.urls')),
    path('about/cars/cars2/', include('xmotors.urls')),
    path('about/cars/cars3/', include('xmotors.urls')),
    path('about/cars/cars2/cars3/car-details/', include('xmotors.urls')),
    path('about/blogs/', include('xmotors.urls')),
    path('about/contact/', include('xmotors.urls')),
    path('about/contact/cars/', include('xmotors.urls')),
    path('about/contact/cars/cars2/cars3/carfl/', include('xmotors.urls')),
    path('about/contact/cars/cars2/cars3/', include('xmotors.urls')),
    path('about/contact/cars/cars2/', include('xmotors.urls')),
    path('about/contact/blogs/', include('xmotors.urls')),
    path('contact/cars/', include('xmotors.urls')),
    path('contact/cars/cars2/car3/carfl/', include('xmotors.urls')),
    path('contact/cars/cars2/cars3/', include('xmotors.urls')),
    path('contact/cars/cars2/', include('xmotors.urls')),
    path('contact/blogs/', include('xmotors.urls')),
    path('car/<int:car_id>/', include('xmotors.urls')),
    path('blog/<int:blog_id>/', include('xmotors.urls')),
    path('checkout/', include('xmotors.urls')),
]
