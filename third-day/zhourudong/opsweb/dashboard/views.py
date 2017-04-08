# coding:utf8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View
from django.template import Context, loader, RequestContext, Template
from django.contrib.auth import authenticate, login, logout





def login_view(request):
    if request.method == "GET":
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})
    elif request.method == "POST":
        ret = {"status": 0}
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        # 验证用户名与密码
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                ret['next_url'] = "/"
            else:
                ret['status'] = 1
                ret['errmsg'] = "用户被禁用"
        else:
            ret['status'] = 2
            ret['errmsg'] = "用户名或密码错误"
        return JsonResponse(ret, safe=True)



def logout_view(request):
    logout(request)
    return HttpResponse("用户退出成功")




class IndexView(View):
    def get(self, requet):
        return render(requet, "public/index.html")

























