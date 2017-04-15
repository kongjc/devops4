# coding:utf8
from django.views.generic import TemplateView, View, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User, Permission, ContentType
from django.http import JsonResponse, HttpResponse, QueryDict, Http404
from django.core import serializers
from django.shortcuts import render
from django.conf import settings

import logging

logger = logging.getLogger('opsweb')


class GroupListView(ListView):
    model = Group
    template_name = 'user/grouplist.html'

    @method_decorator(login_required)
    @method_decorator(permission_required("auth.add_group", login_url=settings.PERMISSION_NONE_URL))
    def post(self, request):
        ret = {'status': 0}
        name = request.POST.get('name', '')
        if name:
            try:
                group = Group()
                group.name = name
                group.save()
            except Exception as e:
                ret['status'] = 1
                ret['ermsg'] = e.args

        return JsonResponse(ret, safe=True)


# 获取用户组信息
class GroupView(View):
    @method_decorator(login_required)
    def get(self, request):
        uid = request.GET.get('uid', '')
        ret = {'status': 0}
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist as e:
            ret['status'] = 1
            ret['errmsg'] = '用户不存在{}'.format(e.args)
        all_groups = Group.objects.all()
        groups = [group for group in all_groups if group not in user.groups.all()]
        return HttpResponse(serializers.serialize("json", groups), content_type="application/json")


# 将用户添加到指定组
class UserGroupView(View):
    ''' 
        显示组下所有的用户列表 
    '''

    @method_decorator(login_required)
    def get(self, request):
        gid = request.GET.get('gid', None)
        try:
            groups = Group.objects.get(pk=gid)
        except Exception as e:
            logging.error('{}'.format(e.args))
            return JsonResponse([], safe=False)
        users = groups.user_set.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'name': user.profile.chinaname} for
                     user in users]
        return JsonResponse(user_list, safe=False)

    """
        将用户添加到指定组
    """

    @method_decorator(login_required)
    @method_decorator(permission_required("auth.add_group", login_url=settings.PERMISSION_NONE_URL))
    def post(self, request):
        ret = {"status": 0}
        uid = request.POST.get('uid', None)
        gid = request.POST.get('gid', None)

        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:

            logger.error("将用户添加至指定用户组，用户不存在，用户id为：{}".format(uid))
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"
            return JsonResponse(ret, safe=True)

        try:
            group = Group.objects.get(pk=gid)
        except Group.DoesNotExist:

            logger.error("将用户添加至指定用户组，用户组不存在，用户组id为：{}".format(uid))
            ret['status'] = 1
            ret['errmsg'] = "用户组不存在"
            return JsonResponse(ret, safe=True)

        user.groups.add(group)
        return JsonResponse(ret, safe=True)

    '''
        将用户从组中删除
    '''

    @method_decorator(login_required)
    def delete(self, request):
        ret = {"status": 0}
        data = QueryDict(request.body)
        uid = data.get('userid', None)
        gid = data.get('groupid', None)
        try:
            user = User.objects.get(pk=uid)
            group = Group.objects.get(pk=gid)
            group.user_set.remove(user)
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


# 组权限管理视图

class GroupPermissionListViwe(TemplateView):
    template_name = 'user/group_permission_list.html'

    def get_context_data(self, **kwargs):
        context = super(GroupPermissionListViwe, self).get_context_data(**kwargs)
        context['group_permission'] = self.get_group_permission()  # 取出现有权限 在模板中匹配 有权限则选中
        context['content_type'] = ContentType.objects.all()  # 取出所有权限
        context['group'] = self.request.GET.get('gid', '')  # 传入组id 提交时获取

        return context

    def get_group_permission(self):
        gid = self.request.GET.get('gid', '')
        try:
            gruop = Group.objects.get(pk=gid)
            # 返回现有权限
            return [per.id for per in gruop.permissions.all()]
        except Group.DoesNotExist as e:
            logger.error('组不存在{0}'.format(e.args))
            return Http404

    @method_decorator(login_required)
    @method_decorator(permission_required("auth.change_group", login_url=settings.PERMISSION_NONE_URL))
    def post(self, request):
        permission_id_list = request.POST.getlist('permission', [])
        groupid = request.POST.get('group', '')
        ret = {"status": 0, "next_url": "/group/list/"}
        try:
            group = Group.objects.get(pk=groupid)  # 取出组
        except Group.DoesNotExist as e:
            logger.error("用户组不存在{}".format(e.args))
            ret['status'] = 1
            ret['errmsg'] = '用户组不存在'
        else:
            if permission_id_list:
                # 取出权限
                permissions_obj = Permission.objects.filter(id__in=permission_id_list)
                # 给组赋予权限
                group.permissions = permissions_obj
        return render(request, settings.TEMPLATE_JUMP, ret)
