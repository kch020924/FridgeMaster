from django.contrib import admin

# Register your models here.
from main.models import users, recipes, items, publish
admin.site.register(users)
admin.site.register(recipes)
admin.site.register(items)
admin.site.register(publish)