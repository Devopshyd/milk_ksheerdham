from django.contrib import admin

from .models import Order,Deliveryboy,Deliveryboy_orders
# Register your models here.

admin.site.register(Order)
admin.site.register(Deliveryboy)
admin.site.register(Deliveryboy_orders)
