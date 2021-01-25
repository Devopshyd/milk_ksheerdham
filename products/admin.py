from django.contrib import admin

from .models import Product,NewArrivals,Driver,Employee,Farm_Data,Flashoffers,Vehicle,Feedback
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(NewArrivals)
admin.site.register(Flashoffers)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Employee)
admin.site.register(Farm_Data)
admin.site.register(Feedback)