from django.contrib import admin

# Register your models here.
from .models import Profile, Location

class LocationAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)