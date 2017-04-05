#-*-coding:utf8-*-
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import  JsonResponse
from django.views.generic import View
from django.template import Context,loader
# Create your views here.

def login_view(request):
    print request.user
    if request.method == 'GET':
        return  render(request,'user/login.html')
    elif request.method == "POST":
        ret = {'status':0}
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                ret['next_url'] = '/'
            else:
                ret['status'] = 1
                ret['errmsg'] = '用户被禁用'
        else:
            ret['status'] = 2
            ret['errmsg'] = '用户名或密码错误'
        return  JsonResponse(ret,safe=True)

class IndexView(View):

    def get(self,request):
        return  render(request, "public/index.html")

