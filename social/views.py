from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request,'index.html')
def choice1(request):
    return render(request,'choice1.html')
def choice(request):
    return render(request,'choice.html')

def signup(request):
    if request.method=="POST":
        Name=request.POST['Name']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

    if User.objects.filter(Name=Name):
        messages.error(request,"Name alreay exit please try again")
        return redirect('index')
    if User.objects.filter(email=email).exists():
        messages.error(request,"email already exist ")
        return redirect('index')
    if len(Name)>10:
        messages.error(request,"Invalid username")
    if password != confirmpassword:
        messages.error(request,"Invalid Password , Please check!!")
             
    return render(request,'signup.html')