from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage


class UserListView(TemplateView):
    template_name = 'user/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        user_list = User.objects.all()
        paginator = Paginator(user_list, 10)
        per_number = 8
        page_range_list = []
        try:
            page = int(self.request.GET.get('page', 1))
            if paginator.num_pages - page >= per_number//2:
                start_index = max(page - per_number//2, 1)
            else:
                start_index = paginator.num_pages - per_number + 1
            end_index = max(page + per_number//2, per_number + 1)
            for number in range(start_index, end_index):
                if 0 < number <= paginator.num_pages:
                    page_range_list.append(number)
            page_obj = paginator.page(page)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context['page_obj'] = page_obj
        context['page_range_list'] = page_range_list
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListView, self).get(request, *args, **kwargs)


class ModifyUserStatusView(View):

    def post(self, request):
        ret = {'status': 0}
        user_id = request.POST.get('user_id', '')
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
        return JsonResponse(ret)
