from django.contrib import admin
from django.urls import path , include
from home import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("search/",views.search, name="search"),
    path("signup/",views.handleSignup, name="handleSignup"),
    path("logout/",views.handleLogout, name="handleLogout"),
    path("login/",views.handleLogin, name="handleLogin"),
]

