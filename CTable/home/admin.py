from django.contrib import admin

# Register your models here.

from .models import Campaign, TextFile

admin.site.register(Campaign)
admin.site.register(TextFile)