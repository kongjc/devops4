from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.contrib.auth.models import User

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


