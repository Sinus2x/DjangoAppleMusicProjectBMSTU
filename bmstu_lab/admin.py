from django.contrib import admin

# Register your models here.
from .models import Albums, Orders, Customers

admin.site.register(Albums)
admin.site.register(Orders)
admin.site.register(Customers)