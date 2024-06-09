from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class items(models.Model):
   
    it_id=models.IntegerField(verbose_name='it_id', primary_key=True, default="invalid")
    it_name=models.CharField(max_length=100, verbose_name='it_name')
    class Meta:
        db_table='items'

class users(models.Model):
    user_mail=models.EmailField(max_length=60, verbose_name='user_mail', primary_key=True, default="invalid")
    user_password=models.CharField(max_length=120, verbose_name='user_password')
    user_name=models.CharField(max_length=60, verbose_name='user_name')
    class Meta:
        db_table='users'


class recipes(models.Model):
    re_id=models.IntegerField(verbose_name='re_id', primary_key=True)
    re_name=models.CharField(max_length=120, verbose_name='re_name')
    re_step=ArrayField(models.CharField(max_length=1000), blank=True, verbose_name='re_step')
    re_minute=models.IntegerField(verbose_name='re_minute')
    # fk_recipes_publisher =models.ForeignKey(users, on_delete=models.CASCADE, default="admin")
    class Meta:
        db_table='recipes'

class publish(models.Model):
    pub_id=models.IntegerField(verbose_name='pub_id', primary_key=True)
    pub_re_id = models.ForeignKey(recipes, on_delete=models.CASCADE, default="none")
    pub_date=models.DateField(verbose_name='pub_date')
    pub_publisher = models.ForeignKey(users, on_delete=models.CASCADE)

class fridge(models.Model):
    fr_id=models.IntegerField(verbose_name='it_id', primary_key=True),
    fr_name=models.CharField(max_length=100, verbose_name='it_name')