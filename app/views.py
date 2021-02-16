from django.shortcuts import render,HttpResponse,redirect
from .models import Posts,Likes
from django.contrib.auth.models import User
from .forms import PostModelForm,RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
# Create your views here.

@login_required(login_url="/login/")
def home(request):
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return render(request,"home.html",context)

@login_required(login_url="/login/")
def add_image(request):
    if request.method =='POST':
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('home')
        else:
            return render(request,'add_posts.html',{'form':form})
    else:
        form = PostModelForm()
        return render(request,'add_posts.html',{'form':form})

@login_required(login_url="/login/")
def like_post(request,id):
    post = Posts.objects.get(id = id)
    user = request.user
    like = Likes.objects.filter(user=user,post=post)
    if like:
        like[0].delete()
        print('disliked')
    else:
        Likes.objects.create(user=user,post=post)
        print('liked')
  
    count = Likes.objects.filter(post=post)
    return HttpResponse(str(len(count)))

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('user name is incorrect')

    return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
         
           
        else:
            return render(request,'register.html',{'form':form})

    else:
        form = RegistrationForm()
       
        return render(request,'register.html',{'form':form})