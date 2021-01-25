from django.contrib import admin

from .models import Address, BillingProfile,Admin
# Register your models here.

admin.site.register(Address)
admin.site.register(BillingProfile)
admin.site.register(Admin)

