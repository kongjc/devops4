from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from dashboard.models import Department

"""
class UserListView(TemplateView):
    template_name = "user/userlist.html"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
       # context['userlist'] = User.objects.all()
        before_range_num = 2
        after_range_num = 3
        userlist = User.objects.all()          # get all userlist object
        paginator = Paginator(userlist, 10)    # instance a Paginator
        page = self.request.GET.get("page", 1) # get the page number
        if int(page) > before_range_num:
            page_range = paginator.page_range[int(page)-before_range_num:int(page)+after_range_num]
        else:
            page_range = paginator.page_range[0:int(page)+after_range_num]
        page_obj = paginator.page(page)        #get the data of the page
        context['page_obj'] = page_obj
        context['page_range'] = page_range
        
        return context

    def get(self, request, *args, **kwargs):
        return super(UserListView, self).get(request, *args, **kwargs)
"""

class UserListView(ListView):
    template_name = "user/userlistl.html"
    model = User
    paginate_by = 10
#    context_object_name = "userlist"
    before_index = 3
    after_index = 2

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
        ret = {"status":0}

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
            ret['errmsg'] = "user not exist"
        return JsonResponse(ret, safe=True)


class ModifyDepartmentView(TemplateView):
    template_name = "user/modify_department.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyDepartmentView, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['user_obj'] = User.objects.get(pk=self.request.GET.get('user', None))
        user_obj = User.objects.get(pk=self.request.GET.get('user', None))
        return context

    def post(self, request):
        user_id = request.POST.get('id', None)
        department_id = request.POST.get('department', None) 
        if not user_id or not department_id:
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)
            department_obj = Department.objects.get(pk=department_id)
        except:
            raise Http404
        else:
            user_obj.profile.department = department_obj
            user_obj.profile.save()
        return redirect("/user/userlist/")

    def get(self, request, *args, **kwargs):
        return super(ModifyDepartmentView, self).get(request, *args, **kwargs)

class ModifyPhoneView(TemplateView):
    template_name = "user/modify_phone.html" 

    def get_context_data(self, **kwargs):
        context = super(ModifyPhoneView, self).get_context_data(**kwargs)
        context['user_obj'] = User.objects.get(pk=self.request.GET.get('user', None))
        user_obj = User.objects.get(pk=self.request.GET.get('user', None))
        print user_obj
        return context

    def get(self, request, *args, **kwargs):
        return super(ModifyPhoneView, self).get(request, *args, **kwargs)

    def post(self, request):
        user_id = request.POST.get('id', None)
        phone = request.POST.get('phone', None)

        if not user_id or not phone:
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)
        except:
            raise Http404
        else:
            user_obj.profile.phone = phone
            user_obj.profile.save()
        return redirect("/user/userlist/")
