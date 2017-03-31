from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404, redirect
from ..models import Department


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


class UserListNewView(ListView):
    template_name = 'user/user_list1.html'
    model = User
    paginate_by = 10
    context_object_name = "user_list"
    page_per_number = 8

    def get_context_data(self, **kwargs):
        context = super(UserListNewView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        return context

    def get_page_range(self, page_obj):
        if page_obj.paginator.num_pages - page_obj.number >= self.page_per_number // 2:
            start_index = max(page_obj.number - self.page_per_number // 2, 1)
        else:
            start_index = page_obj.paginator.num_pages - self.page_per_number + 1
        end_index = max(page_obj.number + self.page_per_number // 2, self.page_per_number + 1)
        return [number for number in range(start_index, end_index) if 0 < number <= page_obj.paginator.num_pages]


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


class ModifyProfileView(TemplateView):
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ModifyProfileView, self).get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        user_id = self.request.GET.get('user_id', -1)
        user = get_object_or_404(User, pk=user_id)
        context['user_obj'] = user
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyProfileView, self).get(request, *args, **kwargs)

    def post(self, request):
        user_id = request.POST.get('user_id', -1)
        profile_name = request.POST.get('profile_name', '')
        profile_phone = request.POST.get('profile_phone', '')
        department_id = request.POST.get('department_id', -1)
        department_obj = get_object_or_404(Department, pk=department_id)
        user_obj = get_object_or_404(User, pk=user_id)
        user_obj.profile.department = department_obj
        user_obj.profile.phone = profile_phone
        user_obj.profile.name = profile_name
        user_obj.profile.save()
        return redirect('/user/list_new/')

