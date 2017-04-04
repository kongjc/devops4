# coding=utf-8

from __future__ import print_function
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
# Create your views here.
from django.template import Context, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, RedirectView, FormView
from django.conf import settings


# def login(request):
#     # template = loader.get_template('user/login.html')
#     # context = Context({"title": "reboot 运维平台"})
#
#     print(request.GET)
#     username = request.POST.get("username", None)
#     print(username)
#     password = request.POST.get("password", None)
#     print(password)
#     return render(request, 'user/login.html', {"title": "reboot 运维平台"})

"""
In [1]: from django.contrib.auth.models import User
In [4]: User.objects.get(username='rock')
Out[4]: <User: rock>

In [5]: user = User.objects.get(username='rock')

In [6]: user.is_active
Out[6]: True

In [7]: user.is_active = False

In [8]: user.save()

In [9]: user.is_active = True

In [10]: user.save()
"""

def login_view(request):
    # 通过 GET/POST 方法获取 QueryDict() 对象
    if request.method == "GET":
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})

    elif request.method == "POST":
        ret = {"status": 0}
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # print(username, password)
        # 对比数据库验证用户名和密码
        user = authenticate(username=username, password=password)

        # 验证成功返回的对象如果存在进行下一步动作
        if user is not None:
            if user.is_active:
                login(request, user)
                ret['next_url'] = '/'
                # return HttpResponse("用户登录成功")
            else:
                ret['status'] = 1
                ret['errmsg'] = "用户已禁用"
                # return HttpResponse("用户登录失败")
        else:
            ret['status'] = 2
            ret['errmsg'] = "密码错误"
            # return HttpResponse("用户登录失败")
        return JsonResponse(ret, safe=True)



class LoginView(View):
    pass


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponse("用户已退出")


def test_form(request):

    if request.method == "GET":
        return render(request, "test/test_form.html")
    elif request.method == "POST":
        """
        request.POST.getlist()
        request.POST.lists()
        request.POST.dict()
        request.POST.get()
        """
        print(request.POST.dict())
        print(request.POST.lists())

        username = request.POST.get('username', '')
        fav = request.POST.getlist('fav')

        print(fav)
        return HttpResponse("")


class IndexView(View):
    # http_method_names = ["get", "post", "delete","reboot"]

    def get(self, request):
        return render(request, "public/index.html")