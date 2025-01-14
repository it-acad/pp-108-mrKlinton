from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_publication', 'count')
    list_filter = ('year_of_publication', 'name')
    search_fields = ('id', 'name', 'description', 'authors__name', 'year_of_publication')
    fieldsets = (
        ("Незмінні дані", { 
            "fields": ("name", "description", "year_of_publication", "authors"),
        }),
        ("Змінні дані", {  
            "fields": ("count", "date_of_issue"),
        }),
    )