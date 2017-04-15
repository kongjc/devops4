# coding:utf8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View
from django.template import Context, loader, RequestContext, Template
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required  # 权限验证
from django.contrib.auth.decorators import login_required  # 登录验证
from django.conf import settings


# import logging
# logger = logging.getLogger('opsweb')


def login_view(request):
    if request.method == "GET":
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})
    elif request.method == "POST":
        ret = {"status": 0}
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 验证用户名与密码
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
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
    # 登录验证装饰器如果不登录直接让其跳转到setting中设置的LOGIN_URL
    @method_decorator(login_required)
    # 如果没有权限就跳转到指定的页面
    @method_decorator(permission_required("dashboard.view_server", login_url=settings.PERMISSION_NONE_URL))
    def get(self, requet):
        # logger.debug('这是首页测试')
        return render(requet, "public/index.html")


# 用户无权限时跳转到此指定页面
def permission(requet):
    return render(requet, 'public/nopermission.html', {})
