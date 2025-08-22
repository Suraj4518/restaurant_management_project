from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModeAdmin):
    list_display = ['id','customer','total_amount','status','created_at']
    list_filter = ['status','created_at']
    search_fields = ['customer_username']

admin.site.register(Order, OrderAdmin)
# Register your models here.
