from django.shortcuts import render, redirect
import re
from django.http import JsonResponse, HttpResponse
from .models import users, recipes
# Create your views here.
def index(request):
    return render(request,'main/index.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try: 
            check_email= users.objects.get(user_mail=email)
        except: 
            check_email= False 
        if not(email and password):
            return HttpResponse("<script>alert('enter both email and password');""location.href='/login/';</script>")
        elif check_email==False:
            return HttpResponse("<script>alert('we cannot find any information under this email');""location.href='/login/';</script>")
        else:
            if password==check_email.user_password:
                request.session["user"]=check_email.user_name
                return HttpResponse("<script>alert('login successed!');""location.href='/home/';</script>")
            else:
                return HttpResponse("<script>alert('wrong password');""location.href='/login/';</script>")
    elif request.method=='GET':
        return render(request,'login/login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

    
def addItem(request):
    user_name=request.session["user"]
    data={}
    data["user_name"] = user_name
    return render(request,'addItem/addItem.html', data)


def create(request):
    user_name=request.session["user"]
    data={}
    data["user_name"] = user_name
   
    if request.method=='POST':
        recipe_id=request.POST['recipe_id']
        # print('레시피 id', recipe_id)
        recipes.objects.create(recipe_id=recipe_id)
        return HttpResponse("<script>alert('success');""location.href='/home/';</script>")
    elif request.method=='GET':
        # print('유저', Users.objects.all()[2].user_name)
        return render(request,'create/create.html', data)

def detail(request, re_id):
    user_name=request.session["user"]
    data={}
    data["user_name"] = user_name
    recipe = recipes.objects.get(re_id=re_id)
    data["recipe"]=recipe
    return render(request,'detail/detail.html', data)

def home(request):
    if request.method=='GET':
        user_name=request.session["user"]
        data={}
        data["user_name"] = user_name
        recipe_list = recipes.objects.all()
        data["recipe_list"]=recipe_list
        return render(request,'home/home.html', data)



def myfridge(request):
    user_name=request.session["user"]
    data={}
    data["user_name"] = user_name
    return render(request,'myfridge/myfridge.html', data)

def signup(request):

    if request.method=='POST':
        user_mail=request.POST['user_mail']
        user_password=request.POST['user_password']
        user_name=request.POST['user_name']
        regex_email='^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex_email, user_mail):
            return HttpResponse("<script>alert('wrong email');""location.href='/signup/';</script>")
        try:
            check_mail = users.objects.get(user_mail=user_mail)
        except:
            check_mail = False
        if check_mail:
            return HttpResponse("<script>alert('this email is already registered');""location.href='/signup/';</script>")
        # Users.objects.create(user_email=user_email, user_password=user_password, user_name=user_name)
        # Users.save()
        newUser=users(user_mail=user_mail, user_password=user_password, user_name=user_name)
        newUser.save()
        return HttpResponse("<script>alert('success');""location.href='/login/';</script>")
    elif request.method=='GET':
       
        return render(request,'signup/signup.html')