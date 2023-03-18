from django.shortcuts import render,redirect
from admin_app.admin_signup import Adminsignup
from admin_app.models import Admin_signup,CreateEvent
from django.contrib import messages
from admin_app.eventform import EventForm
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def admin_signin(request):
    if request.method == 'POST':

        password = request.POST.get('password')
        Name = request.POST.get('Name')
        user = Admin_signup.objects.filter(password=password, Name=Name).count()
        print("____", user)

        if user == 1:
            user = Admin_signup.objects.filter(password=password, Name=Name)
            for l1 in user:
                request.session['Name'] = l1.Name
                request.session['id'] = l1.id
                print(l1.Name)
                request.session['id'] = l1.id
                return redirect('/show')
        else:
            messages.error(request, 'Invalid Name and password')
        return render(request, 'admin_signin.html')
    else:
        return render(request, 'admin_signin.html')

def admin_signup(request):
    if request.method=="POST":
        form=Adminsignup(request.POST)
        try:
            form.save()
            return redirect('/admin_signin')
        except:
            pass

    else:
        form=Adminsignup()
        context={'form':form}
        return render(request,'admin_signup.html',context)


def test(request):  
    if request.method == "POST":  
        form = EventForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EventForm()  
    return render(request,'test.html',{'form':form})  
def show(request):  
    event = CreateEvent.objects.all()  
    return render(request,"show.html",{'event':event})
def destroy(request, id):  
    event = CreateEvent.objects.get(id=id)  
    event.delete()  
    return redirect("/show")    