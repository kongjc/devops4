#!/usr/bin/python
# coding=utf8

from django.views.generic import View, TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User, Permission, ContentType
from django.http import JsonResponse, HttpResponse, QueryDict, Http404
from django.core import serializers
from django.shortcuts import render
from django.conf import settings

# log
import logging
logger = logging.getLogger("opsweb")


class GroupListView(ListView):
    """用户组展示逻辑"""
    model = Group
    template_name = "user/grouplist.html"

    @method_decorator(login_required)
    @method_decorator(permission_required("dashboard.view_group", login_url=settings.PERMISSION_NONE_URL))
    def post(self, request):
        """处理【用户组】请求逻辑"""
        ret = {"status": 0}
        name = request.POST.get("name", None)       # 获取 QueryDict 中，后端传过来的 name 值
        if name:
            try:
                group = Group()
                group.name = name
                group.save()
            except Exception as e:
                ret['status'] = 1
                ret['errmsg'] = e.args

        return JsonResponse(ret, safe=True)


class GroupView(View):
    """
    取用户组信息
    """
    def get(self, request):
        """处理【用户添加到组】模态框内的获取组信息 逻辑"""
        uid = request.GET.get('uid')        # 取前端传递的 uid
        ret = {"status": 0}
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"

        all_groups = Group.objects.all()    # 所有用户组
        user_groups = user.groups.all()     # 用户所在组

        # 列表生成器, 用来判断 当前组不在 all_groups 里，则用户添加到用户组的时候，给用户展示该组信息
        groups = [group for group in all_groups if group not in user_groups]

        # 序列化 groups 返回给前端
        return HttpResponse(serializers.serialize("json", groups), content_type="application/json")


class UserGroupView(View):
    """"""
    def get(self, request):
        """取出指定用户组下的成员信息"""
        gid = request.GET.get('gid', None)          # 获取前端传递的 gid
        try:
            group = Group.objects.get(pk=gid)       # 根据 gid 查询 group
        except:
            return JsonResponse([], safe=False)
        users = group.user_set.all()                # 取出组下的所有用户列表对象

        # 列表推导式转换格式，像前端传递指定格式的数据
        user_list = [{"username": user.username, "email":user.email, "name":user.profile.name, "id":user.id} for user in users]
        return JsonResponse(user_list, safe=False)

    def post(self, request):
        """处理【用户添加到用户组】逻辑"""
        ret = {'status':0}          # 返回值
        # print(request.POST)
        uid = request.POST.get('uid', None)
        gid = request.POST.get('gid', None)
        try:
            user = User.objects.get(pk=uid)     # 取user name
        except User.DoesNotExist:
            logger.error(" 将用户添加到指定的用户组，用户不存在，用户 id 为: {0}".format(uid))
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"

        try:
            group = Group.objects.get(pk=gid)   # 取group name
        except Group.DoesNotExist:
            logger.error(" 将用户添加到指定的用户组，用户不存在，用户 id 为: {0}".format(uid))
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"

        user.groups.add(group)                   # 将对应的用户添加到用户组
        return JsonResponse(ret, safe=True)

    @method_decorator(login_required)
    @method_decorator(permission_required("dashboard.change_group", login_url=settings.PERMISSION_NONE_URL))
    def delete(self, request):
        """将用户从用户组中删除"""
        ret = {"status": 0}         # 返回信息
        # 获取 QueryDict 字典信息，<QueryDict: {u'userid': [u'300'], u'groupid': [u'6']}>
        data = QueryDict(request.body)
        # print(data)
        uid = data.get('userid', None)
        gid = data.get('groupid', None)
        try:
            user = User.objects.get(pk=uid)
            group = Group.objects.get(pk=gid)
            group.user_set.remove(user)     # 根据获取的 userid，groupid 取回对应的 user，group 并进行 remove
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"
        except Group.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户组不存在"
        except Exception as e:
            ret['status'] = 1
            ret['errmsg'] = e.args

        return JsonResponse(ret, safe=True)


class GroupPermissionListView(TemplateView):
    """用户组权限视图"""
    template_name = "user/group_permission_list.html"

    def get_context_data(self, **kwargs):
        """向前端传递数据"""
        context = super(GroupPermissionListView, self).get_context_data(**kwargs)
        context['group'] = self.request.GET.get('gid', None)        # 传递 group
        context['content_type'] = ContentType.objects.all()         # 传递 content_type 对象
        context['group_permissions'] = self.get_group_permission()   # 传递 group_permission 对象
        return context

    @method_decorator(login_required)
    @method_decorator(permission_required("dashboard.view_group", login_url=settings.PERMISSION_NONE_URL))
    def post(self, request):
        """处理 【修改用户组权限】 post 请求逻辑"""
        # print(request.POST)
        permission_id_list = request.POST.getlist('permission', [])         # 获取权限列表
        groupid = request.POST.get('group', None)                           # 获取前端传递的 groupid 变量
        ret = {"status": 0, "next_url": "/group/list"}                      # 返回值
        try:
            group = Group.objects.get(pk=groupid)
        except Group.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = "用户组不存在"
        else:
            if permission_id_list:
                permission_objs = Permission.objects.filter(id__in=permission_id_list)  # 根据 permission_id 返回对应权限 name
                group.permissions = permission_objs             # 将勾选的权限赋予该组
        return render(request,  settings.TEMPLATE_JUMP, ret)

    def get_group_permission(self):
        """获取 group permission 的逻辑"""
        gid = self.request.GET.get('gid', None)     # 取前端传递过来的 gid
        try:
            group = Group.objects.get(pk=gid)
            return [per.id for per in group.permissions.all()]
        except Group.DoesNotExist:
            raise Http404









