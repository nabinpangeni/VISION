from django.contrib import admin
from django.urls import path , include
from blog import views
urlpatterns = [
    path('', views.blogHome, name='blogHome'), 
    path("translate/",views.translate_app,name='trans'),
    path("summer/",views.summer,name='summer'),
    path("postComment",views.postComment,name="postComment"), 
    path('<str:slug>', views.blogPost, name='blogPost'),
]
