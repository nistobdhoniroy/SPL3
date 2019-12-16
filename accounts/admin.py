from django.contrib import admin
from .models import Seller, User, Customer

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'email', 'is_seller', 'is_customer')


admin.site.register(User, UserAdmin)
admin.site.register(Seller)
admin.site.register(Customer)