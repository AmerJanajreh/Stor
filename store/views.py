from django.shortcuts import render,redirect
from .models import Product,Category,Order,Customer
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
categories = Category.objects.all()

def home(request):
    products = Product.objects.all()
    return  render(request ,'home.html' , {'products' : products ,'categories' : categories})
def about(request):
    return render(request , 'about.html',{'categories': categories})


def login_user(request ):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None :
            login(request , user)
            messages.success(request , ('you have been logged in'))
            return redirect('home')
        else:
            messages.success(request ,  ('Thera was in error ,  please try again ')) 
    else:
        return  render(request ,'login.html',{'categories': categories})
       
    return  render(request ,'login.html' , {'categories': categories})
def logout_user(request):
    logout(request)
    messages.success(request,('you have been logged Thank for stopping by .......'))
    return redirect('home')


def register_user (request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() :
            print('a')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username ,password = password)
            login(request , user)
            messages.success(request , ('you have been logged in'))
            return redirect('home')
        else:
            messages.success(request , ('Whoops ther was a problem Registering , pleas try again '))
            return redirect('home')
    else:
        return  render(request ,'register.html',{'form':form,'categories': categories})

def  product(request,pk):
    product = Product.objects.get(id=pk)
    categories = Category.objects.all()
    return  render(request ,'product.html' , {'product' : product,'categories': categories})




def category(request , foo):
    foo = foo.replace('-' , ' ')
    try:
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request , 'category.html' , {'products': products , 'category'  : category ,'categories': categories})
    except:
       messages.success(request , ("Taht Cateory Doesn't Exit " ))
       return redirect('home')
   
    return None
