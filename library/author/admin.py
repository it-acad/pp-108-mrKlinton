from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')  
    search_fields = ('name', 'surname', 'patronymic') 
    list_filter = ('name', 'surname') 
    ordering = ('surname',) 

    fieldsets = ( 
        ("Основна інформація", {"fields": ("name", "surname", "patronymic")}),
        ("Додаткові дані", {"fields": ("books",)}),
    )

    filter_horizontal = ('books',)  