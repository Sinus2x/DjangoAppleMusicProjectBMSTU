from django.contrib import admin

# Register your models here.
from .models import Albums, Orders, Customers, AlbumsOrders

admin.site.register(Albums)
admin.site.register(Orders)
admin.site.register(Customers)
admin.site.register(AlbumsOrders)