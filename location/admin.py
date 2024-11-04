from django.contrib import admin

# Register your models here.

from .models import Country, State, City, Locality, Landmark, Area, Address 

admin.site.register(Country)
admin.site.register(State)