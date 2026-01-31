from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .utilities import rGenerator
from .models import ShortedUrl, AdditionalUserInfo

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info("Invalid Username or Password")
            return redirect('login')
    return render(request, 'login.html')

def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Already Exists")
                return redirect('signup')

            user = User.objects.create_user(username = username, first_name = fname, last_name = lname, email = email)
            user.set_password(password1)
            user.save()
            AdditionalUserInfo.objects.create(user = request.user)
        else:
            messages.info("Password doesn't match")
            return redirect('signup')
        messages.info("Account Created Successfully")
        return redirect('home')

        
    return render(request, 'signup.html')

@login_required
def home_page(request):
    created = True
    if request.method  == 'POST':
        long_url = request.POST.get('long_url')
        alias = request.POST.get('alias')
        
        if not alias:
            alias = rGenerator()
            while(ShortedUrl.objects.filter(alias = alias).exists()):
                alias = rGenerator()
        else:
            if (ShortedUrl.objects.filter(alias = alias).exists()):
                messages.info("Alias Already Exists")
                created = False

        if created:
            ShortedUrl.objects.create(long_url = long_url, alias = alias)
            return redirect('dashboard')


        
    return render(request, 'home.html')



@login_required
def dashboard_page(request):
    all_urls = ShortedUrl.objects.all()
    return render(request, 'dashboard.html', {'urls' : all_urls, 'total_urls' : all_urls.count()})

@login_required
def profile_page(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic')
        user = User.objects.get(username  = request.user.username)
        user.first_name = fname 
        user.last_name = lname
        user.email = email
        user.save()

        Additional_Info, create = AdditionalUserInfo.objects.get_or_create(user = request.user)
        if profile_pic:
                Additional_Info.profile_pic = profile_pic
                Additional_Info.save()

    return render(request, 'profile.html')



def redirector(request, alias):
    try:
        url = get_object_or_404(ShortedUrl, alias = alias)
        url.no_of_clicks+=1
        url.save()
        return redirect(url.long_url)
    except:
        return render(request, 'nosuchurl.html')
@login_required
def delete_url(request, id):
    url = get_object_or_404(ShortedUrl, id = id)
    url.delete()
    return redirect('dashboard')


def logout_page(request):
    logout(request)
    return redirect ('home')