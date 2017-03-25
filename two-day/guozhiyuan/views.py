#coding=utf8
from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User

# Create your views here.

class UserLogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                ret =  {'status': 0,'next_url': '/opsweb/'}
            else:
                ret = {'status':1, 'errmsg':'用户已锁定'}
        else:
            ret = {'status':1, 'errmsg':'用户名或密码错误'}
        return JsonResponse(ret, safe=True)


class UserListView(View):
    def get(self,request):
        users = User.objects.all()

        pages = Paginator(users, 5)
        page = request.GET.get('page',1)
        try:
            page_obj = pages.page(page) #取当前页的数据
        except EmptyPage:
            page_obj = pages.page(1)
        return render(request, 'userlist.html', {'users':users, 'page_obj':page_obj})

class ModifyUserStatusView(View):
    def post(self,request):
        ret = {'status':0}
        user_id = request.POST.get('user_id',None)
        try:
            user = User.objects.get(id=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = '用户不存在'
        return JsonResponse(ret, safe=True)