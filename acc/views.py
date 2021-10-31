from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


# Create your views here.
def index(request):
    return render(request, 'acc/index.html')


def userlogin(request):
    un = request.POST.get('username')
    pw = request.POST.get('password')
    user = authenticate(username = un, password = pw)
    if user:
        login(request, user)
    return redirect('acc:index')


def userlogout(request):
    logout(request)
    return redirect('acc:index')

def signup(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        com = request.POST.get('comment')
        pic = request.FILES.get('pic')
        User.objects.create_user(username = un, password = pw, comment = com, pic=pic)
        return redirect('acc:index')
    return render(request, 'acc/signup.html')

def userinfo(request):
    return render(request, "acc/info.html")

def userdel(request):
    u = User.objects.get(username = request.user.username)
    u.delete()
    return redirect("acc:index")

def usermod(request):
#     u = User.objects.get(username = request.user.username)

#     if request.method == "POST": #수정할 데이터 입력
#         un = request.POST.get('username')
#         pw = request.POST.get('password')
#         com = request.POST.get('comment')
#         pic = request.FILES.get('pic')

#         return redirect('acc:userinfo')

#     context = { #수정할 곳으로 이동
#         'u':u
#     }
    return render(request, "acc/mod.html")