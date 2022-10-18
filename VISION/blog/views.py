from http.client import HTTPResponse
from django import forms
from django.shortcuts import render ,redirect, HttpResponse
from requests import post
from .models import BlogComment
from .models import Postblog
from django.contrib import messages
from gtts import gTTS
from gTTS.templatetags.gTTS import say

from googletrans import Translator

#An empty array called textForTts



# Create your views here.
def blogHome(request):
    allPosts=Postblog.objects.all()
    
    context={'allPosts':allPosts}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = Postblog.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post)
    context={"post":post,"comments":comments }
    return render(request,"blog/blogPost.html",context)

def postComment(request):
    if request.method=="POST":

        comments=request.POST.get("comments")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Postblog.objects.get(sno=postSno)
        
        comments=BlogComment(comment=comments,user=user,post=post)
    comments.save()
    messages.success(request,"Your comment has been posted successfully")
    return redirect(f"/blog/{post.slug}")

#reference for summerizing a blog 
def translate_app(request):
    if request.method=="POST":
        lang=request.POST.get("lang")
      
        translator=Translator()
        tr=translator.translate("my name is nabin",dest='de')
        tr.text
        return redirect(f"/blog/{Postblog.slug}",{"result":tr.text})
    return redirect(f"/blog/{Postblog.slug}")