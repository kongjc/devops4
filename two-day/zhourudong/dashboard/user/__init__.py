#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/3/22 18:06
# Author: zhourudong
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator


class UserListView(TemplateView):
    template_name = 'user/userlist.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        userlist = User.objects.all()

        paginator = Paginator(userlist, 10)  # 实例化paginator
        ''' 显示的页面范围  [1...10] * 10 '''
        page_numbers_range = 10
        ''' 总页面数量 '''
        page_count = paginator.num_pages
        ''' 获取当前第几页, 默认为第1页(页码数) '''
        page = self.request.GET.get("page", 1)
        start_index = (int(page) - 1) / page_numbers_range * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= page_count:
            end_index = page_count

        '''(获取当前页到末尾页码 列表形式) '''
        page_index = paginator.page_range[start_index:end_index]
        ''' 获取page对象(获取当前页的数据 到末尾页码) '''
        page_obj = paginator.page(page)
        context['page_obj'] = page_obj
        context['page_index'] = page_index
        print type(context['page_obj'])
        print page_index
        return context


def get(self, request, *args, **kwargs):
    self.request = request  # 当前第几页
    return super(UserListView, self).get(request, *args, **kwargs)


class ModifyUserStatusView(View):
    def post(self, request):

        user_id = request.POST.get('user_id', None)
        try:
            user = User.objects.get(pk=user_id)
            ret = {'status': 0}
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = '用户不存在'
        return JsonResponse(ret, safe=True)
