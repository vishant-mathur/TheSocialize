from django.shortcuts import render,redirect
from admin_app.admin_signup import Adminsignup
from admin_app.models import Admin_signup,CreateEvent
from django.contrib import messages
from admin_app.events import EventForm
from django.views.decorators.csrf import csrf_exempt


def event(request):
    form = CreateEvent.objects.all()
    return render(request,"event.html",{'form':form})
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
                return redirect('/')
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
def test(request,id):
    sam = CreateEvent.objects.filter(id=id)
    
    if request.method=="POST":
        form=EventForm(request.POST)
        if request.POST.get('event_name') and request.POST.get('event_address') and request.POST.get('date_time') and request.POST.get('event_dis') and request.POST.get('event_type'):
            matrix=CreateEvent()
            
            matrix.event_name=request.POST.get('event_name')
            matrix.event_address=request.POST.get('event_address')
            matrix.date_time=request.POST.get('date_time')
            matrix.event_dis=request.POST.get('event_dis')
            matrix.event_type=request.POST.get('event_type')          
        try:
            form.save()
            # matrix.save()
            return redirect('/')
        except:
            pass
    else:
        form=EventForm()
    context={
        'sam':sam,
    }
    return render(request,"eventform.html",context)
