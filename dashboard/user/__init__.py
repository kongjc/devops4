# coding=utf8
from django.views.generic import TemplateView, View, ListView, RedirectView
from django.shortcuts import render, Http404, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from paginator import getPages
from dashboard.models import Department
from dashboard.models import Profile


"""
class UserListView(TemplateView):

    template_name = "user/userlist.html"

    # 给模板传数据，固定格式 kkk
    def get_context_data(self, **kwargs):
        content = super(UserListView, self).get_context_data(**kwargs)
        # 遍历数据库用户赋予 content
        userlist = User.objects.all()           # 获取所有用户列表对象

        # 通过 getPages 函数传递给页面一个字典 {page_obj: page_obj}
        contents = getPages(self.request, userlist, content)
        return contents


    def get(self, request, *args, **kwargs):
        return super(UserListView, self).get(request, *args, **kwargs)
"""


class UserListView(ListView):

    template_name = "user/userlist.html"
    model = User
    paginate_by = 10        # 每页展示多少对象
    before_index = 4        # 当前页往前几页
    after_index = 3         # 当前页往后几页
    # context_object_name = "userlist"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        # 覆盖父类的属性
        context['page_range'] = self.get_page_range(context['page_obj'])
        return context

    def get_page_range(self, page_obj):
        """分页处理逻辑"""

        # 开始序列号 = 当前页码号 - 后置序列号
        start_index = page_obj.number - self.before_index
        # 应对开始序列异常的情况，最小不能为 0
        if start_index < 0:
            start_index = 0

        # 最终在页面上供展示的循环的 list
        page_range = page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]
        return page_range


class ModifyUserStatus(View):

    def post(self, request):
        ret = {'status': 0}         # user 的默认状态
        user_id = request.POST.get('user_id', None)     # 从 request 中获取 user_id
        # print(user_id)
        # 根据用户 id 获取用户的 is_active 状态，并赋予对应的值
        try:
            user = User.objects.get(pk=user_id)

            # 这里注意一旦前端点击按钮，将会修改 is_active 状态，所以修改的值和用户的 is_active 是相反的
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()     # 保存到 DB

        # 童虎不存在的提示和错误信息
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"

        return JsonResponse(ret, safe=True)


class ModifyDepartmentView(TemplateView):
    """
    修改页面部门功能
    """
    template_name = "user/modify_department.html"

    # 重写并覆盖父类 get_context_data 方法和 context 属性
    def get_context_data(self, **kwargs):
        context = super(ModifyDepartmentView, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.all()            # 给前端传递 departments 对象
        # context['user_obj'] = User.objects.get(pk=self.request.GET.get('user', None))
        context['user_obj'] = get_object_or_404(User, pk=self.request.GET.get('user', None))    # 向前端传递 user_obj 对象
        return context

    def post(self, request):
        """ 处理 post 请求 """
        user_id = request.POST.get('id', None)              # 获取前端传递的 user_id
        department_id = request.POST.get('department', None)    # 获取前端传递的 department_id

        # 如果上述两个值任何一个为空，直接返回 404
        if not user_id or not department_id:
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)     # 根据前端传递的 user_id 获取在数据库中获取用户信息
            department_obj = Department.objects.get(pk=department_id)   # 根据前端传递的 depart_id 获取部门的信息
        except:
            raise Http404
        else:
            # 当不存在异常的情况，进行修改部门的操作
            user_obj.profile.department = department_obj        # 将前端传递的部门信息覆盖原值（即修改部门)
            user_obj.profile.save()         # 保存到 profile 表，注意不是 user 表

        return redirect("/user/list")       # 点击完跳转用户展示页

    def get(self, request, *args, **kwargs):
        """ 处理 get 请求 """
        self.request = request
        return super(ModifyDepartmentView, self).get(request, *args, **kwargs)


class ModifyPhoneViewTmp(TemplateView):

    template_name = "user/modify_phone_tmp.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyPhoneViewTmp, self).get_context_data(**kwargs)
        # context['user_obj'] = User.objects.get(pk=self.request.GET.get('user', None))
        # user_profile = Profile()
        # user_profile.user = User.objects.get(pk=self.request.GET.get('user', None))     # 关联 user 表的 user 和 profile user
        context['user_obj'] = get_object_or_404(User, pk=self.request.GET.get('user', None))    # 向前端传递 user_obj 对象
        # context['user_profile'] = user_profile       # 向前端传递 profile 信息

        return context

    def post(self, request):
        """ 处理 post 请求 """
        # print(request.POST)
        user_id = request.POST.get('id', None)              # 获取前端传递的 user_id
        new_phone = request.POST.get('new_phone', None)             # 获取前端传递的 new_phone 值

        # 如果上述两个值任何一个为空，直接返回 404
        if not user_id or not new_phone:
            raise Http404
        try:
            user_obj = User.objects.get(pk=user_id)     # 根据前端传递的 user_id 获取在数据库中获取用户信息
        except:
            raise Http404
        else:
            # 当不存在异常的情况，进行修改部门的操作
            user_obj.profile.phone = new_phone        # 将前端传递的部门信息覆盖原值（即修改部门)
            user_obj.profile.save()         # 保存到 profile 表，注意不是 user 表

        return redirect("/user/list")       # 点击完跳转用户展示页

    def get(self, request, *args, **kwargs):
        """ 处理 get 请求 """
        self.request = request
        return super(ModifyPhoneViewTmp, self).get(request, *args, **kwargs)


class ModifyCNnameViewTmp(TemplateView):
    """
    
    """
    template_name = "user/modify_cnname_tmp.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyCNnameViewTmp, self).get_context_data(**kwargs)
        context['user_obj'] = get_object_or_404(User, pk=self.request.GET.get('user', None))

        return context

    def post(self, request):
        # print(request.POST)
        user_id = request.POST.get('id', None)              # 获取前端传递的 user_id
        cn_name = request.POST.get('cn_name', None)             # 获取前端传递的 new_phone 值

        # 如果上述两个值任何一个为空，直接返回 404
        if not user_id or not cn_name:
            raise Http404
        try:
            user_obj = User.objects.get(pk=user_id)     # 根据前端传递的 user_id 获取在数据库中获取用户信息
        except:
            raise Http404
        else:
            # 当不存在异常的情况，进行修改部门的操作
            user_obj.profile.cn_name = cn_name        # 将前端传递的信息覆盖原值（即修改中文名)
            user_obj.profile.save()         # 保存到 profile 表，注意不是 user 表

        return redirect("/user/list")       # 点击完跳转用户展示页

    def get(self, request, *args, **kwargs):
        """ 处理 get 请求 """
        self.request = request
        return super(ModifyCNnameViewTmp, self).get(request, *args, **kwargs)