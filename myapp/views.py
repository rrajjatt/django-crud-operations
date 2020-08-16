from django.shortcuts import render,redirect
from myapp.forms import *
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def registeruser(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = RegisterUserForm()
            return render(request,'myapp/registeruser.html',{'form':form})
    else:
        form = RegisterUserForm()
        return render(request,'myapp/registeruser.html',{'form':form})

def showall(request):
    form = RegisterUser.objects.all()
    return render(request,'myapp/showall.html',{'form':form})

def edituser(request,id):
    result = RegisterUser.objects.get(id=id)
    form = RegisterUserForm(instance=result)
    if request.method=='GET':
        return render(request,'myapp/edituser.html',{'form':form,'result':result})
    else:
        form = RegisterUserForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            return redirect('showall')
        else:
            return render(request,'myapp/edituser.html',{'form':form,'result':result, 'error':'Bad data passed'})


    
'''def updateuser(request,id):
    result = RegisterUser.objects.get(id=id)
    if request.method=="POST":
        form = RegisterUserForm(request.POST,instance=result)
        if form.is_valid():
            form.save()
            return redirect('showall')
    else:
        form = RegisterUserForm(request.POST,instance=result)
    return render(request,'myapp/edituser.html',{'form':form,'result':result,'error':'Bad data passed'})
'''
def deleteuser(request,id):
    result = RegisterUser.objects.get(id=id)
    if request.method=='POST':
        result.delete()
        return redirect('showall')