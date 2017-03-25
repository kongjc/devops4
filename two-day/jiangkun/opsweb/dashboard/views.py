# coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View

import json
from django.template import Context, loader, Template
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def hello(request):
    # attributions
    print request
    print request.scheme
    print request.method
    print request.GET
    print request.META
    print "path_info", request.path_info
    print "path", request.path
    print "body", request.body
    print "encoding", request.encoding
    # requestContextGggquest.POST
    print "user", request.user
    # methods
    print request.get_host()
    print request.get_full_path()
    print request.build_absolute_uri()
    # print request.get_signed_cookie("name")
    print request.is_secure()
    print request.is_ajax()

    # exe
    data = {"name": "rock", "age": "25"}

    #return HttpResponse("<h1>Hello world!!! 你好！！</h1>")
    #return HttpResponse(data, content_type="application/json")
    return HttpResponse(json.dumps(data), content_type="application/json", status=200)
    #return JsonResponse(data, safe=True)
    #return JsonResponse(data, safe=False)

    data_list = ["a", "b", "c"]
    #return JsonResponse(data_list, safe=False)
    #return JsonResponse(data_list, safe=True)


def login_view(request):
    #template = loader.get_template("user/login.html")
    #context = Context({"title": "reboot 运维平台"})
    #return HttpResponse(template.render(context))
    
    # RequestContext
    #template = loader.get_template("user/login.html")
    #context = RequestContext(request, {"title": "reboot 运维平台"})
    #return HttpResponse(template.render(context))

    #reboot = {"name": "seer", "age": 27}
    # user 已经有全局对象了，不能随便乱用
    #user = {"reboot": {"name": "seer", "age": 27}}
    #reboot = {"reboot": {"name": "seer", "age": 27}}
    #template = Template("<h1>login: {{ reboot.name }} --- {{ reboot.age }}</h1>")
    #context = RequestContext(request, reboot)
    #return HttpResponse(template.render(context))

    #
    #print request.GET
    #print request.POST
    #username = request.GET.get("username", None)
    #username = request.POST.get("username", None)
    #print username
    #password = request.GET.get("password", None)
    #password = request.POST.get("password", None)
    #print password

    ## all in render
    #return render(request, 'user/login.html', {"title": "reboot 运维平台"})

    if request.method == "GET":
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})
    elif request.method == "POST":
        ret = {"status": 0}
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #print username
        #print password
        # 验证用户名与密码
        user = authenticate(username=username, password=password)
        print user
        try:
            if user is not None:
                if user.is_active:
                    # 将用户信息写入session
                    # 将session_key 写入cookie
                    ret["next_url"] = "/"
                    login(request, user)
                    # return HttpResponse("用户登录成功")
                else:
                    ret["status"] = 1
                    ret["errmsg"] = "该用户被禁用"
                    # return HttpResponse("该用户被禁用")
            else:
                ret["status"] = 2
                ret["errmsg"] = "用户登录失败"
                # return HttpResponse("用户登录失败")
            return JsonResponse(ret, safe=True)
        except Exception as e:
            print e

        # if username == "rock" and password == "654321":
        #     return HttpResponse("登录成功")
        # else:
        #     return HttpResponse("登录失败:")


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})

    def post(self, request):
        ret = {"status": 0}
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print username
        # print password
        # 验证用户名与密码
        user = authenticate(username=username, password=password)
        print user
        try:
            if user is not None:
                if user.is_active:
                    # 将用户信息写入session
                    # 将session_key 写入cookie
                    ret["next_url"] = "/"
                    login(request, user)
                    # return HttpResponse("用户登录成功")
                else:
                    ret["status"] = 1
                    ret["errmsg"] = "该用户被禁用"
                    # return HttpResponse("该用户被禁用")
            else:
                ret["status"] = 2
                ret["errmsg"] = "用户登录失败"
                # return HttpResponse("用户登录失败")
            return JsonResponse(ret, safe=True)
        except Exception as e:
            print e


# def logout_view(request):
#     # 删除session_key
#     logout(request)
#     return HttpResponse("用户退出成功")


class LogoutView(View):
    def get(self, request):
        return redirect("/login/")


def test_form(request):
    # return HttpResponse("form 表单")
    print request.body

    if request.method == "GET":
        return render(request, 'test/test_form.html')
    elif request.method == "POST":
        print request.POST
        # <QueryDict: {u'username': [u'rock'], u'fav': [u'1', u'2']}>
        # 要给默认值，否则返回为空，会出错
        username = request.POST.get('username', "")
        print username

        # get 只返回一个值
        # fav = request.POST.get('fav')
        # 多个值 要用 getlist()
        # 要给默认值，否则返回为空，会出错
        fav = request.POST.getlist('fav', [])
        print fav

        # QueryDict.dict()
        print request.POST.dict()

        # QueryDict.lists()
        print request.POST.lists()
        return HttpResponse("")
    else:
        print request.body
        print QueryDict(request.body)

        data = QueryDict(request.body)
        fav = data.get("fav[]", "")
        print fav
        return HttpResponse("")


# class IndexView(View):
#     http_method_names = ["get", "delete", "reboot"]
#
#     def get(self, request):
#         return HttpResponse("")
#
#     def post(self, request):
#         return HttpResponse("")
#
#     def delete(self, request):
#         return HttpResponse("")
#
#     def reboot(self, request):
#         return HttpResponse("")

class IndexView(View):
    def get(self, request):
        return render(request, "public/index.html")

