# coding:utf-8
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse

from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage

# __init__.py 写views，其他文件写业务逻辑（方法）
class UserListView(TemplateView):
    template_name = "user/userlist.html"

    def get_context_data(self, **kwargs):
        # get_context_data 获取数据，传到模板
        context = super(UserListView, self).get_context_data(**kwargs)
        # 获取所有的用户列表对象
        userlist = User.objects.all()
        # context['user_list'] = User.objects.all()

        # 实例化Paginator对象
        paginator = Paginator(userlist, per_page=10)
        # 获取当前第几页（页码数）
        page = self.request.GET.get("page", 1)
        # 获取当前页的数据 --> Page对象
        try:
            page_obj = paginator.page(page)
        except EmptyPage:
            page_obj = paginator.page(1)
            context['status'] = "1"
            context['errmsg'] = "页码为空"

        context['page_obj'] = page_obj
        return context

    # get 可以不写，如果写要写成如下固定样子
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListView, self).get(request, *args, **kwargs)


class ModifyUserStatusView(View):
    def post(self, request):
        ret = {"status": 0}
        user_id = request.POST.get("user_id", None)
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



