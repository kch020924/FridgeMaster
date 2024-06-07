from django.db import models

# Create your models here.

class Users(models.Model):
    user_email=models.EmailField(max_length=100, verbose_name='user_email')
    user_password=models.CharField(max_length=120, verbose_name='user_password')
    user_name=models.CharField(max_length=60, verbose_name='user_name')
    class Meta:
        db_table='Users'

class Recipe(models.Model):
    recipe_id=models.CharField(max_length=100, verbose_name='recipe_id')
    
    class Meta:
        db_table='Recipe'

class Item(models.Model):
    item_name=models.CharField(max_length=100, verbose_name='item_name')
    
    class Meta:
        db_table='Item'