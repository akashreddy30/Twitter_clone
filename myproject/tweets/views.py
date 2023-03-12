from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tweet
from .models import UserProfile
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        profile = UserProfile(user=username, mobile=request.POST['mobile'])
        profile.save()
        user.save()
        

        return redirect('login')
    else:
        return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            text="INVALID CREDENTIALS"
            messages.info(request,text)
            return render(request,'registration/success.html')
    else:
        return render(request,'registration/login.html')
def profile(request):
    print(request.user)
    user_profile = User.objects.get(username=request.user)
    up=UserProfile.objects.get(user=request.user)
    context = {'user_profile': user_profile,'up':up}
    return render(request, 'registration/profile.html', context)

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        s=Tweet()
        s.username=str(request.user)
        s.content=content
        s.save()
        return redirect('profile')
    else:
        return render(request, 'registration/create_tweet.html')

@login_required
def list_tweets(request):
    tweets = Tweet.objects.filter(username=str(request.user)).values()
    return render(request, 'registration/list_tweets.html', {'tweets': tweets})

@login_required
def delete_tweet(request,content):
    tweet = Tweet.objects.filter(username=str(request.user),content=content)
    tweet.delete()
    text="THE TWEET IS SUCCESSFULLY DELETED"
    messages.info(request,text)
    return render(request,'registration/success.html')
def home(request):
    return render(request,'registration/home.html')
