
from optparse import TitledHelpFormatter
from django.shortcuts import render,HttpResponse,redirect
from responses import POST
from home.models import Contact
from django.contrib import messages
from blog.models import Postblog
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request ):
    return render(request,"home/home.html")

def contact(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST["content"]   
        if len(name)<3 or len(email)<6 or len(phone)<8 or len(content)<5:
            messages.error(request,"Please Submit Detail Correctly")
        else:
            contact=Contact(name=name,email=email,content=content,phone=phone)
            contact.save()
            messages.success(request,"Details Sent Successfully.")

    return render(request,"home/contact.html")

    
def about(request ):
    return render(request,"home/about.html")
#For get search 
def search(request):
    query=request.GET["search"]
    allPosts=Postblog.objects.filter(title__icontains=query)
    params={"allPosts":allPosts}
    return render(request,"home/search.html",params)
#write for search post 


def handleSignup(request):
    if request.method=='POST':
    
       # get the post parameter
        user_name=request.POST["user_name"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        #check foe errorneous inputs
        if len(user_name)>10:
            messages.error(request,"username must be lessthan 10")
            return redirect ("home")
   
        if pass1!=pass2:
            messages.error(request,"password must be same on both")
            return redirect ("home")
        if not user_name.isalnum():
            messages.error(request,"username must be alphanumeric")
            return redirect ("home")                   
        
        #Create the user
        myuser=User.objects.create_user(user_name,email,pass1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request,"your VISION account has been successfully Created")
        return redirect ("home") 
    else:
        return HttpResponse("404 Not-Found")
#for login method 
def handleLogin(request ):
    if request.method=="POST":
        login_username=request.POST["login_username"]
        login_pass=request.POST["login_pass"]
    #authentication of user
        User=authenticate(username=login_username,password=login_pass)
        if User!=None:
            login(request,User)
            messages.success(request,"LoggedIn successfully ")
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("home")
    return HttpResponse("404-Not Found")
#for logout method 
def handleLogout(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect("home")
