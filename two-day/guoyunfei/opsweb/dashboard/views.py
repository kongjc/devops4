from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                ret = {'status': 0, 'next_url': '/'}
            else:
                ret = {'status': 1, 'errmsg': '禁止登录'}
        else:
            ret = {'status': 2, 'errmsg': '用户名或密码错误'}
        return JsonResponse(ret)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class IndexView(View):

    def get(self, request):
        return render(request, 'public/index.html', {'title': 'ops_web'})
