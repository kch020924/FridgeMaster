from django.contrib import admin

# Register your models here.
from main.models import Users, Recipe, Item
admin.site.register(Users)
admin.site.register(Recipe)
admin.site.register(Item)