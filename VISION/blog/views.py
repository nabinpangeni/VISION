from http.client import HTTPResponse
from django import forms
from django.shortcuts import render ,redirect, HttpResponse
from requests import post

from blog.code import SentimentAnalyzer
from .models import BlogComment
from .models import Postblog
from django.contrib import messages
from .summer import generate_summary
from gtts import gTTS
from gTTS.templatetags.gTTS import say

from googletrans import Translator
from .code import SentimentAnalyzer
#An empty array called textForTts
'''def speech(request):
    if request.method=="POST":
        lang=request.POST.get("lang")
        data=request.POST.get("content")
        obj = say(language=lang, text=data)
        return HttpResponse({'obj':obj})
    #return render(request, 'index.html', {'obj':obj})
    return redirect(f"/blog/{Postblog.slug}")'''

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
        data=request.POST.get("content")
        translator=Translator()
        tr=translator.translate(data,dest=lang)
        # return redirect(f"/blog/{Postblog.slug}",{"result":tr.text})
        return HttpResponse(tr.text)
    return redirect(f"/blog/{Postblog.slug}")
def summer(request):
    if request.method=="POST":
        data=request.POST.get("content")
        sr=generate_summary(data)
        # return redirect(f"/blog/{Postblog.slug}",{"result":tr.text})
        print(sr)
        return HttpResponse(sr)
    return redirect(f"/blog/{Postblog.slug}")

    '''def SentimentApp(request):
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence
            textAns = SentimentAnalyzer(sent)
            context['text'] = textAns
    
    context['comments'] = comments
    return render(request, '{Postblog.slug}', context=context)'''

def sentiment(request):
    if request.method=="POST":
        # sent_data=request.POST.get("comment")
        postSno=request.POST.get("postSno")
        sent_data=BlogComment.objects.filter(post=postSno)
        #see=BlogComment.objects.filter()
        # print(sent_data)
        score = []   
        for i in sent_data:
            score.append(SentimentAnalyzer(i.post.content))
        
        # print(sent_req)
        if (sum(score)/len(score))>0.7:
            return HttpResponse('Sentiment is:  Positive')
        else:
            return HttpResponse('Sentiment is:  Negative')
    return redirect(f"/blog/{Postblog.slug}")