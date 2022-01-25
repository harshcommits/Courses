from django.contrib import admin
from .models import Pet

@admin.register(Pet)  #this takes model class as argument
class PetAdmin(admin.ModelAdmin):
     list_display = ['name', 'species', 'breed', 'age', 'sex']
