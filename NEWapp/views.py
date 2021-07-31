from django.shortcuts import render,redirect
from NEWapp.models import Document
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from NEWapp.forms import Savenote

# Create your views here

@login_required
def editor(request):
    documents=Document.objects.filter(contactholder=request.user)
    if request.method=="POST":
        form=Savenote(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=False).contactholder=request.user
            form.save()
    return render(request,'editor.html',{'documents':documents})


def UserLogin(request):
    return render(request,'userlogin.html')

def RegisterPage(request):
    return render(request,'registerpage.html')

@csrf_exempt
def register(request):
    username=request.POST['user_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
   

    if password==confirm_password:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/RegisterPage/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already Taken')
            return redirect('/RegisterPage/')
        else:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            messages.info(request,'User Created')
            return redirect('/RegisterPage/')
    else:
        messages.info(request,'Password Not Matching')
        return redirect('/RegisterPage/')
    return render(request,'registerpage.html')

@csrf_exempt
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        print(username)
        if user is not None:
            auth.login(request,user)
            return redirect("/editor/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/UserLogin/')
    else:
        return render(request,'userlogin.html')

@login_required
def destroy(request,id):
    fees=Document.objects.get(pk=id)
    fees.delete()
    return redirect('/editor/')

def logout(request):
    auth.logout(request)
    return redirect('/RegisterPage/')


def update(request,id):
    if request.method == "POST":
        doc=Document.objects.get(pk=id)
        form=Savenote(request.POST,request.FILES,instance=doc)
        if form.is_valid():
            form.save(commit=False).contactholder=request.user
            form.save()
            return redirect('/editor/')

    else:
        docu = Document.objects.get(pk=id)
        return render(request,'updateedit.html',{'document':docu})