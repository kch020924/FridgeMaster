from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('login.html/', views.login, name='login'),
    path('addItem.html/', views.addItem, name='addItem'),
    path('create.html/', views.create, name='create'),
    path('detail.html/', views.detail, name='detail'),
    path('home.html/', views.home, name='home'),
    path('myfridge.html/', views.myfridge, name='myfridge'), 
    path('signup.html/', views.signup, name='signup'),
]