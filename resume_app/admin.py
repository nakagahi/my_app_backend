from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import User

# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    pass