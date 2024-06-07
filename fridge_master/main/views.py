from django.shortcuts import render
import re
from django.http import JsonResponse, HttpResponse
from .models import Users, Recipe
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def login(request):
    return render(request,'login/login.html')
    
def addItem(request):
    return render(request,'addItem/addItem.html')

def create(request):
    if request.method=='POST':
        recipe_id=request.POST['recipe_id']
        print('레시피 id', recipe_id)
        Recipe.objects.create(recipe_id=recipe_id)
        return HttpResponse("<script>alert('success');""location.href='/home.html/';</script>")
    elif request.method=='GET':
        # print('유저', Users.objects.all()[2].user_name)
        return render(request,'create/create.html')

def detail(request):
    return render(request,'detail/detail.html')

def home(request):
    if request.method=='GET':
        print('레시피!!!!', Recipe.objects.all())
        return render(request,'home/home.html')
    

def myfridge(request):
    return render(request,'myfridge/myfridge.html')

def signup(request):

    if request.method=='POST':
        user_email=request.POST['user_email']
        user_password=request.POST['user_password']
        user_name=request.POST['user_name']
        regex_email='^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex_email, user_email):
            return HttpResponse("<script>alert('wrong email');""location.href='/signup.html/';</script>")
        Users.objects.create(user_email=user_email, user_password=user_password, user_name=user_name)
        return HttpResponse("<script>alert('success');""location.href='/home.html/';</script>")
    elif request.method=='GET':
        # print('유저', Users.objects.all()[2].user_name)
        return render(request,'signup/signup.html')