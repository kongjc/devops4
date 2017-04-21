# coding:utf8
import datetime
import base64

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View
from django.template import Context, loader, RequestContext, Template
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required  # 权限验证
from django.contrib.auth.decorators import login_required  # 登录验证
from django.conf import settings


import logging
logger = logging.getLogger('opsweb')

def encode_base64(string):
    string = string.strip()
    # 加随机字符
    s = base64.b32encode(string + "123Qweabc")
    return s


def decode_base64(string):
    s = base64.b32decode(string)
    # 去掉随机字符
    return s[:-9]


def login_view(request):
    if request.method == "GET":
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})

    elif request.method == "POST":
        """
            使用cookie登录
                1、第一次登录记住密码 cookie为空需要检查
        """
        ret = {"status": 0}
        username = request.POST.get("username", None)
        remember_pwd = request.POST.get("remember_pwd", 0)

        # 是否有登录历史
        has_save = request.COOKIES.get("has_login", 0)
        if str(has_save) == '1':
            password = request.COOKIES.get("password", None)
            try:
                password = decode_base64(password)
            except Exception as e:
                logger.error('密码解析错误{}'.format(e.args))
        else:
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

        response_data = JsonResponse(ret, safe=True)

        # 使用记住密码
        if str(remember_pwd) == '1':
            # 使用timedelta 防止时间异常 32号等等
            time_ = datetime.datetime.now() + datetime.timedelta(days=1)

            # 设置过期时间 每天凌晨 2点0分0秒0毫秒
            time_ = time_.replace(hour=2, minute=0, second=0, microsecond=0)
            # 对密码进行加密
            password_ = encode_base64(password)
            response_data.set_cookie("password", password_, expires=time_)
            response_data.set_cookie("username", username, expires=time_)
            # 标识是否已经登录历史
            response_data.set_cookie("has_login", '1', expires=time_)

        return response_data


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
