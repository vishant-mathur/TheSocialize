from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from social.models import User_signup
from django.contrib import messages
from django import forms  
from django.views.decorators.csrf import csrf_exempt
from social.user_signin import Usersignup




def index(request):
    return render(request,'index.html')
def choice1(request):
    return render(request,'choice1.html')
def choice(request):
    return render(request,'choice.html')

@csrf_exempt
def signin(request):
    if request.method == 'POST':

        password = request.POST.get('password')
        Name = request.POST.get('Name')
        user = User_signup.objects.filter(password=password, Name=Name).count()
        print("____", user)

        if user == 1:
            user = User_signup.objects.filter(password=password, Name=Name)
            for l1 in user:
                request.session['Name'] = l1.Name
                request.session['id'] = l1.id
                print(l1.Name)
                request.session['id'] = l1.id
                return redirect('/')
        else:
            messages.error(request, 'Invalid Name and password')
        return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method=="POST":
        form=Usersignup(request.POST)
        try:
            form.save()
            return redirect('/signin')
        except:
            pass

    else:
        form=Usersignup()
        context={'form':form}
        return render(request,'signup.html',context)
