# coding:utf8
import re
from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.auth.models import User
from dashboard.models import Department, Profile

from django.core.paginator import Paginator, EmptyPage

"""
class UserListView(TemplateView):
    template_name = "user/userlist.html"
    before_index = 6
    after_index = 5

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        userlist = User.objects.all()           # 获取所有的用户列表对象
        paginator = Paginator(userlist, 10)     # 实例化Paginator
        page = self.request.GET.get("page", 1)  # 获取当前第几页（页码数）
        try:
            page_obj = paginator.page(page)         # 获取当前页的数据（）
        except EmptyPage:
            page_obj = paginator.page(1)
        context['page_obj'] = page_obj
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        context['page_range'] = page_obj.paginator.page_range[start_index : page_obj.number + self.after_index ]
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListView, self).get(request, *args, **kwargs)

"""


class UserListView(ListView):
    template_name = "user/userlistl.html"
    model = User
    paginate_by = 10
    before_index = 6
    after_index = 5

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        return context

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]


class ModifyUserStatusView(View):
    def post(self, request):
        ret = {"status": 0}

        user_id = request.POST.get('user_id', None)
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"
        return JsonResponse(ret, safe=True)


class ModifyDepartmentView(TemplateView):
    template_name = "user/modify_department.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyDepartmentView, self).get_context_data(**kwargs)
        context['user_obj'] = get_object_or_404(User, pk=self.request.GET.get('user', None))
        context['departments'] = Department.objects.all()

        return context

    def post(self, request):
        user_id = request.POST.get('id', None)
        department_id = request.POST.get('department', None)
        if not user_id or not department_id:
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)
            # 通过id 查询用户
            department_obj = Department.objects.get(pk=department_id)
            # 通过id查询部门
        except:
            # 查询不到结果则报错
            raise Http404
        else:
            # 修改部门的的id,后保存
            user_obj.profile.department = department_obj
            user_obj.profile.save()
        return redirect("/user/userlist/")

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyDepartmentView, self).get(request, *args, **kwargs)


class ModifyUserPhoneView(TemplateView):
    template_name = "user/modify_userphone.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyUserPhoneView, self).get_context_data(**kwargs)
        context['user_obj'] = get_object_or_404(User, pk=self.request.GET.get('user', None))
        context['profile'] = Profile.objects.get(id=self.request.GET.get('user', None))

        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyUserPhoneView, self).get(request, *args, **kwargs)
    
    def post(self, request):
        user_id = request.POST.get('id', None)
        # 获取手机号码
        profile_phone = request.POST.get('phone', None)
        if not user_id or not profile_phone:
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)

            REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
            p_regex = re.compile(REGEX_MOBILE)
            if p_regex.match(profile_phone):
                pass
            else:
                raise ValueError("手机格式错误")
        except Exception as e:
            print(e)
            raise Http404
        else:
            # 外键
            user_obj.profile.phone = profile_phone
            user_obj.profile.save()
        return redirect("/user/userlist/")


