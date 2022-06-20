
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from matplotlib.style import context
from .models import UserTask

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        obj = UserTask.objects.all().filter(user=request.user)
        context={'tasks':obj}
        return render(request,'home.html',context)
    else:
        return redirect('/register')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/register')
    else:
        return redirect('/register')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            try:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect('/')
            except Exception as e:
                return redirect('/register')
        else:
            return redirect('/register')
    else:
        return redirect('/register')

def signout(request):
    logout(request)
    return redirect('/')

def add(request):
    if request.method=="POST":
        title=request.POST['title']
        user = UserTask(user=request.user,title=title)
        user.save()
        return redirect('/')
    else:
        return redirect('/')

def status(request,id):
    task = UserTask.objects.get(id=id)
    current=task.complete
    task.complete=not current
    task.save()
    return redirect('/')
def delete(request,id):
    task=UserTask.objects.all().filter(id=id)
    context={'tasks':task}
    if request.method=="POST":
        task.delete()
        return redirect('/')
    else:
        return render(request,'confirm_delete.html',context)

def edit(request,id):
    if request.method=="POST":
        task=UserTask.objects.get(id=id)
        newtitle=request.POST['newtitle']
        task.title=newtitle
        task.save()
        return redirect('/')
    else:
        return render(request,'edit.html')



    

