from django.shortcuts import render, redirect
from .forms import Signupform, Loginform, Createblogfrom
from django.urls import reverse
from .models import Signup, Blog

# Create your views here.

def Signupview(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            myusername = form.cleaned_data.get('username')
            myemail = form.cleaned_data.get('password')
            check_if_user_exists = Signup.objects.filter(username = myusername).exists()
            check_if_email_exists = Signup.objects.filter(email_address = myemail).exists()
            form.save()
            return redirect('login')
    else:
        form = Signupform
    return render(request, 'users/signup.html', {'form': form})


def Loginview(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        #print(form.cleaned_data.get('username'))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            #context = {'username': username}
            return redirect('home-user')
    else:
        form = Loginform
    return render(request, 'users/login.html', {'form': form})


def Homeview(request):
    return render(request, 'users/home.html')

def Userhomeview(request):
    blog = Blog.objects.all
    #blog.username = Loginview.username
    return render(request, 'users/home-user.html', {'blog': blog})


def Createblogview(request):
    if request.method == 'POST':
        form = Createblogfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-user')
    else:
        form = Createblogfrom
    return render(request, 'users/create-blog.html', {'form': form})


def Viewblogview(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'users/view-blog.html', {'blog': blog})


'''
def Editblogview(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'users/update-blog.html', {'blog': blog})
'''

def Updateblogview(request, id):
    blog = Blog.objects.get(id = id)
    form = Createblogfrom(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home-user')
    return render(request, 'users/update-blog.html', {'blog': blog})


def Deleteblogview(request, id):
    blog = Blog.objects.get(id = id)

    blog.delete()
    return redirect('home-user')