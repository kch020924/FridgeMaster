from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('addItem/', views.addItem, name='addItem'),
    path('create/', views.create, name='create'),
    path('detail/<int:re_id>', views.detail, name='detail'),
    path('home/', views.home, name='home'),
    path('myfridge/', views.myfridge, name='myfridge'), 
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout,  name='logout')
]