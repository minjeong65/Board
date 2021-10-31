from django.shortcuts import render,redirect
from .models import Board
from django.utils import timezone
from acc.models import User
from django.core.paginator import Paginator
# from .models import Home

# Create your views here.
def home(request):
    page = request.GET.get('page',1)
    cate= request.GET.get('cate','')
    kw = request.GET.get('kw','')
    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith = kw)

        elif cate == 'wri':
            b = Board.objects.filter(writer=kw)
        elif cate == "con":
            b = Board.objects.filter(content__contains = kw)
    else:
        b = Board.objects.all()
    
    b = b.order_by('-ctime')
    pag = Paginator(b,10)
    obj = pag.get_page(page)

    context= {
        'blist':obj,
        "cate":cate,
        'kw':kw,

    }
    return render(request, 'hm/home.html',context)


def create(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        wri = request.user.username
        con = request.POST.get("content")
        Board(subject=sub, writer=wri, content=con, ctime=timezone.now()).save()
        return redirect('home:home')
    return render(request, 'hm/create.html')


def detail(request,bpk):
    b = Board.objects.get(id = bpk)
    u = User.objects.get(username = b.writer)
    context = {
        'b':b,
        'pic': u.getpic()
    }
    return render(request, 'hm/detail.html', context)


def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if b.writer() == request.user.username:
        b.delete()
    else:
        return render(request, 'error/forbidden.html')
    
    return redirect('hm:home')


def modify(request, bpk):
    b = Board.objects.get(id = bpk)
    if b.writer != request.user.username:
        return render(request, "error/forbidden.html")
    if request.method == "POST":
        sub =request.POST.get("subject")
        con =request.POST.get('content')
        b.subject = sub
        b.content = con
        b.save()
        return redirect('home:detail',bpk=bpk)
    context = {
        'b':b
    }
    return render(request, 'hm/modify.html', context)

#좋아요
def addup(request, bpk):
    b = Board.objects.get(id=bpk)
    u = User.objects.get(username = request.user.username)
    b.up.add(u)
    return redirect("home:detail", bpk=bpk)

#좋아요 취소
def removeup(request, bpk):
    b = Board.objects.get(id=bpk)
    u = User.objects.get(username = request.user.username)
    b.up.remove(u)
    return redirect("home:detail", bpk=bpk)