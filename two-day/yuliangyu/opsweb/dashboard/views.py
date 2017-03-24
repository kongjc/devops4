#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


import json

# Create your views here.

"""
def hello(request):
    return HttpResponse("<h1>hello world</h1>")
    data = {"name":"rula","age":25}
    data_list = ["a","b","c"]
    return JsonResponse(data_list,safe=False)


def login_view(request):
    #template = loader.get_template('user/login.html')
    #context = Context({'title': "reboot platform"})
    #return HttpResponse(template.render(context))
    if request.method == "GET":
        return render(request,'user/login.html',{"title":"reboot platform"})
    elif request.method == "POST":
        ret = {"status": 0}
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print username
        print password
        #validate username and password
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            print "user is not None"
            if user.is_active:
                login(request,user)
                ret['next_url'] = "/"
            else:
                ret['status'] = 1
                ret['errmsg'] = "username is lock"
#                return HttpResponse("login failed")
        else:
            ret['status'] = 2
            ret['errmsg'] = "username or password error"
            print "user is None"
        return JsonResponse(ret, safe=True)

def logout_view(request):
    logout(request)
    return HttpResponse("user logout success")

"""


class LoginView(View):
    def get(self, request):
        return render(request, "user/login.html", {"title":"reboot platform"})

    def post(self, request):
        ret = {"status": 0}
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request,user)
                ret['next_url'] = "/"
            else:
                ret['status'] = 1
                ret['errmsg'] = "user is lock"
        else:
            ret['status'] = 2
            ret['errmsg'] = "username or password error"
        return JsonResponse(ret, safe=True)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse("user logout success")


def test_form(request):
    if request.method == "GET":
        return render(request,"test/test_form.html")
    elif request.method == "POST":
        print request.POST
        username = request.POST.get("username")
        print username
        fav = request.POST.getlist('fav',[])
        print fav
        return HttpResponse("")

class IndexView(View):
    def get(self, request):
        return render(request, "public/index.html")
