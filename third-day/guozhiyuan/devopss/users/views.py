#coding=utf8
from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.forms.models import model_to_dict
from django.views.generic import View,ListView
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse,JsonResponse
from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from users.models import *
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


# class UserListView(View):
#     def get(self,request):
#         users = User.objects.all()
#
#         pages = Paginator(users, 5)
#         page = request.GET.get('page',1)
#         try:
#             page_obj = pages.page(page) #取当前页的数据
#         except EmptyPage:
#             page_obj = pages.page(1)
#         return render(request, 'userlist.html', {'users':users, 'page_obj':page_obj})
class UserListView(ListView):
    template_name = 'userlist.html'
    model = User
    paginate_by = 5
    before_index = 6
    after_index = 5

    departments = Department.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView,self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        context['departments'] = self.departments
        return context

    def get_page_range(self,page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return list(page_obj.paginator.page_range)[start_index: page_obj.number + self.after_index] #要用list转换下,否则类型是xrange将无法序列化

class ModifyUserInfoView(View):
    def get(self,request):
        user_id = request.GET.get('user_id','')
        try:
            user = User.objects.get(id=user_id)
            user = model_to_dict(user)
            try:
                user_profile = Profile.objects.get(user=user_id)
                user_profile = (model_to_dict(user_profile))
            except:
                ret = {'status':0,'user':user,'user_profile':{}}
                return JsonResponse(ret)
            ret = {'status':0,'user':user,'user_profile':user_profile}
            return JsonResponse(ret)
        except:
            pass

    def post(self,request):
        try:
            id = request.POST.get('id','')
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            title = request.POST.get('title','')
            phone = request.POST.get('phone','')
            department =  request.POST.get('department','')

            user = User.objects.get(id=id)
            user_profile = Profile.objects.get(user=id)
            d = Department.objects.get(id=department)


            user.email = email
            user.save()
            user_profile.title = title
            user_profile.phone = phone
            user_profile.name = name
            user_profile.department = d
            user_profile.save()

            res = {'status':0}
            return JsonResponse(res)
        except:
            res = {'status':1}
            return JsonResponse(res)


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