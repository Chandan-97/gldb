from django.contrib import admin

from .models import Profile, Product, Service, ProductHierarchy, ProfileExtension
# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(ProductHierarchy)
admin.site.register(ProfileExtension)