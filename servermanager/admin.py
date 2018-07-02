from django.contrib import admin
# Register your models here.
from .models import commands


class CommandsAdmin(admin.ModelAdmin):
    list_display = ('title', 'command', 'describe')
