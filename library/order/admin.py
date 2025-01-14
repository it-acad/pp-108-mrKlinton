from django.contrib import admin
from .models import Order



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('created_at', 'end_at')
    

