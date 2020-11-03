from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
def index(request):
    return render(request,'index.html')

def handleSignup(request):
    if request.method=='POST':
        #Get post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        #email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #check for inputs error
        if len(username)>10:
            messages.error(request,"Your username must be under  10 character")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request,"Password does not match")
            return redirect('home')
        # print(username)
        # messages.success(request,"Your account has been successfully created")
        # return redirect('home')
        #create user
        else:
            myuser= User.objects.create_user(username,username,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('home')

    else:
        return HttpResponse('404 - Not allowed')

def handleLogin(request):
    if request.method=='POST':
        #Get post parameters
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        print(loginusername)
        print(loginpass)
        user  = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,"Successful Logged In")
            return redirect('home')
        else :
            messages.error(request,"Invalid credentials")
            return redirect('home')
    return HttpResponse('404 - Not found')
def handleLogout(request):
        logout(request)
        messages.success(request,"Successful Logged Out")
        return redirect('home')