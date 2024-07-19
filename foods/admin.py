from django.contrib import admin

from foods.models import *

# Register your models here.

admin.site.register(Food)
admin.site.register(Category)