from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import signpageform, todoform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def loginpage(request):
    if request.method =='POST':
        sm = AuthenticationForm(request=request, data=request.POST)
        if sm.is_valid():
            uname = sm.cleaned_data['username']
            upass = sm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/index/')
    else:
        sm = AuthenticationForm()            
    return render(request,'login.html',{'sms':sm})

def signuppage(request):
    if request.method == 'POST':
        fm = signpageform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    else:
        fm = signpageform()        
    return render(request,'signup.html',{'fms':fm})

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/')    

@login_required
def home(request):
    if request.user.is_authenticated:
        user = request.user
        sf = todoform()
        todos = todo.objects.filter(user=user)
        return render(request,'index.html',{'sfs':sf,'todos':todos})
    else:
        return HttpResponseRedirect('/')



@login_required
def showtodo(request):
    if request.user.is_authenticated:
        user = request.user
        sf = todoform(request.POST)
        if sf.is_valid():
            todo = sf.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')

        else:
            sf=todoform()
            return render(request,'index.html') 
    return HttpResponseRedirect('/')       


def delete(request,id):
    # if request.method == 'POST':
        pi = todo.objects.get(pk = id)
        pi.delete()
        return redirect('/index/')

def changestatus(request,id,status):
    x = todo.objects.get(pk = id)
    x.status = status
    x.save()
    return redirect('/index/')       

    