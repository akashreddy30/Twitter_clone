"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweets import views

urlpatterns = [
    path("",views.home,name='/'),
    path("home/",views.home,name="home"),
    path("admin/", admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('create_tweet/',views.create_tweet, name='create_tweet'),
    path('list_tweets/',views.list_tweets, name='list_tweets'),
    path('delete_tweet/<str:content>',views.delete_tweet, name='delete_tweet'),
    path('profile/', views.profile, name='profile'),
]
