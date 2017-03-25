#!/usr/bin/env python
#-*- coding:utf8 -*-
from  django.views.generic import  TemplateView,View
from  django.contrib.auth.models import User
from  django.http import JsonResponse
from  django.core.paginator import Paginator

class  UserListView(TemplateView):
    template_name = 'user/userlist.html'

    def get_context_data(self, **kwargs):
        context =  super(UserListView,self).get_context_data(**kwargs)
        #context['userlist'] = User.objects.all() ##获取所有用户列表对象
        userlist = User.objects.all()
        paginator = Paginator(userlist,10)
        page = self.request.GET.get('page',1)
        try:
            page_obj = paginator.page(page)
        except EmptyPage:
            page_obj = paginator.page(1)
        context['page_obj'] = page_obj
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        #TemplateView.get(self,request,*args,**kwargs)
        #self.get(request,*args,**kwargs)
        return super(UserListView,self).get(request, *args, **kwargs)

class ModifyUserStatusView(View):
    def post(self,request):
        ret = {'status':0}
        user_id = request.POST.get('user_id',None)
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            ret['status'] = 1
            ret['errmsg'] = '用户不存在'
        return JsonResponse(ret,safe=True)