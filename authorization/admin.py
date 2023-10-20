from django.contrib import admin

from .models import Person


# Register your models here.
@admin.register(Person)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
    ]
    ordering = ['name']
