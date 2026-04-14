from django.contrib import admin
from .models import Car
from .models import Blog
from .models import Contact
from .models import About
from .models import Seller

# Register your models here.
admin.site.register(Car)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Seller)
