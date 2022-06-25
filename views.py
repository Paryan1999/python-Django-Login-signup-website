from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from .models import Blog,Profile
from .forms import Profile_forms


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username/Password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def home(request):
        aryan = Blog.objects.all()
        if request.method=="POST":
            search=request.POST['search']
            result=Blog.objects.filter(blog_heading__icontains=search) #search for specific word/heading 
            return render(request,'base.html',{'aryan':result})# result ek variable lekr aryan ke sath show krwa diya  
        else:
            return render(request,'base.html',{'aryan':aryan})

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']    
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user= User.objects.create_user(first_name=first_name,last_name=last_name , username=username,email=email,password=password1)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'Password didnt match')
            return redirect('register')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
#Profile

def profile(request,id=0):
    if request.method=="GET":
        if id==0:
            show=Profile_forms()
        else:
            d=Profile.objects.get(pk=id)
            show=Profile_forms(instance=d)
        return render(request,'profile.html',{'show':show})
    else:
        if id==0:
            show=Profile_forms(request.POST,request.FILES)
        else:
            d=Profile.objects.get(pk=id)
            show=Profile_forms(request.POST,request.FILES,instance=d)
        if show.is_valid():
            show.save()
            messages.info(request,'send data')
        return render(request,'profile.html',{'show':show})
    
def Show_profile(request):
    data=Profile.objects.all()
    return render(request,'show_profile.html',{'data':data})


def wip(request):
    return render(request,'wip.html')