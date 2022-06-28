import os

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from app.form import FileForm
from app.models import User, Resource, nocheck


def blog_login(request):
    if request.method == "GET":
        return render(request, 'blog_login.html')
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    users = User.objects.filter(name=username)
    if users.count():
        user = users.first()
        #     取数据  last() 也可以
        if user.password == password:
            return render(request, 'index.html')
        else:
            messages.error(request, '用户名或密码不正确')
            return HttpResponseRedirect(reverse('blog_login'))
    else:
        messages.error(request, '未注册,请先注册！！！')
        return HttpResponseRedirect(reverse('blog_login'))


def blog_list(request):
    t = 'Moki'
    return render(request, 'blog_list.html',{"t":t})


def blog_edit(request):
    return render(request, 'blog_edit.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    phone = request.POST.get("phone")
    # print(user,pwd,phone)

    User.objects.create(name=user, password=pwd, phone=phone)
    return render(request, 'blog_login.html')


# def sql():
def index(request):
    return render(request, 'index.html')


def resource(request):
    r1 = Resource.objects.all()
    return render(request, 'resource.html', {"r1": r1})


def info_list(request):
    user=User.objects.all()
    return render(request, 'info_list.html', {"user": user})


def info_delete(request):
    nid = request.GET.get("nid")
    User.objects.filter(id=nid).delete()
    return redirect("info_list")


def page_list(request):
    data_list = Resource.objects.all()
    return render(request, 'page_list.html',{"data_list": data_list})


def info_delete1(request):
    nid = request.GET.get("nid")
    Resource.objects.filter(id=nid).delete()
    return redirect("page_list")


def info_delete2(request):
    nid1 = request.GET.get("nid1")
    Resource.objects.filter(id=nid1).delete()
    return redirect("resource")


def page_add(request):
    # if request.method == "GET":
    #     return render(request, 'page_add.html')
    # title = request.POST.get("user")
    # body = request.POST.get("body")
    # author = request.POST.get("phone")
    #
    # Resource.objects.create(title=title, body = body, author=author)
    # return render(request, 'page_list.html')
    c1 = nocheck.objects.all()
    return render(request, 'page_add.html', {"c1": c1})


def mindex(request):
    return render(request, 'mindex.html')


def mblog_list(request):
    return render(request,'mblog_list.html')


def pindex(request):
    return render(request, 'pindex.html')


def pedit(request):
    return render(request, 'pedit.html')


def plist(request):
    return render(request, 'plist.html')


def nlist(request):
    return render(request, 'nlist.html')


def p_i(request):
    if request.method == "GET":
        return render(request, 'person_information.html')
    return render(request, 'blog_list.html')


def nedit(request):
    return render(request,'nedit.html')


def community(request):
    return render(request,'community.html')


def fp(request):
    if request.method == "GET":
        return render(request, 'fp.html')
    return render(request,'blog_login.html')