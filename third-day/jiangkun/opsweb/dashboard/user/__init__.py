# coding:utf-8
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage

from dashboard.models import Department


# __init__.py 写views，其他文件写业务逻辑（方法）
class UserListViewManual(TemplateView):
    """
    手写分页
    """
    template_name = "user/userlist.html"
    before_index = 5
    after_index = 5

    def get_context_data(self, **kwargs):
        # get_context_data 获取数据，传到模板
        context = super(UserListView, self).get_context_data(**kwargs)
        # 获取所有的用户列表对象
        userlist = User.objects.all()
        # context['user_list'] = User.objects.all()

        # 实例化Paginator对象，每页显示10条
        paginator = Paginator(userlist, per_page=10)
        # 获取当前第几页（页码数）
        page = self.request.GET.get("page", 1)
        # 获取当前页的数据 --> Page对象
        try:
            # 当前是0页，会有异常
            page_obj = paginator.page(page)
        except EmptyPage:
            page_obj = paginator.page(1)
            context['status'] = "1"
            context['errmsg'] = "页码为空"

        context['page_obj'] = page_obj
        # list
        print page_obj.paginator.page_range
        # current page number
        print page_obj.number
        # print page_obj.paginator.page_range[page_obj.number - self.before_index: page_obj.number + self.after_index]

        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        context['page_range'] = page_obj.paginator.page_range[start_index: page_obj.number+self.after_index]
        return context

    # get 可以不写，如果写要写成如下固定样子
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListViewManual, self).get(request, *args, **kwargs)


class UserListView(ListView):
    """
    ListView 重做用户列表和分页
    """
    # userlistl.html 模板
    template_name = "user/userlistl.html"
    # 数据源
    model = User
    # 分页条数 10
    paginate_by = 10
    # context_object_name = "userlist"
    before_index = 5
    after_index = 5

    def get_context_data(self, **kwargs):
        # 首先执行父类的get_context_data()，再重写子类的get_context_data()内容
        context = super(UserListView, self).get_context_data(**kwargs)
        page_obj = context["page_obj"]
        context['page_range'] = self.get_paage_range(page_obj=page_obj)
        return context

    def get_paage_range(self, page_obj):
        """
        处理分页
        :param page_obj:
        :return:
        """
        print "page_range列表 {}".format(page_obj.paginator.page_range)
        print "当前页 {}".format(page_obj.number)

        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]

    # def get(self, request, *args, **kwargs):
    #     super(UserListView, self).get(*args, **kwargs)


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


class ModifyDepartmentView(TemplateView):
    template_name = "user/modify_department.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyDepartmentView, self).get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        # context["user_obj"] = User.objects.get(pk=self.request.GET.get('user', None))
        # 处理id 不存在 显示404页面
        # user_obj 是modify_department.html 调用的变量 －－ 变量名称要一致
        # context["user"] = get_object_or_404(User, pk=self.request.GET.get('user', None))
        context["user_obj"] = get_object_or_404(User, pk=self.request.GET.get('user', None))
        return context

    def post(self, request):
        user_id = request.POST.get('id', None)
        department_id = request.POST.get('department', None)
        # print "user_id: {}, department_id: {}".format(user_id, department_id)
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

        # return HttpResponse("")
        return redirect("/user/userlist/")

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyDepartmentView, self).get(request, *args, **kwargs)


class ModifyPhoneView(TemplateView):
    template_name = "user/modify_phone.html"

    def get_context_data(self, **kwargs):
        context = super(ModifyPhoneView, self).get_context_data(**kwargs)
        context["user_obj"] = get_object_or_404(User, pk=self.request.GET.get('user', None))
        # print context["user_obj"]
        return context

    def post(self, request):
        user_id = request.POST.get('id', None)
        phone = request.POST.get('phone', None)
        print user_id, phone
        if not user_id or not phone:
            raise Http404

        if len(phone) > 11:
            # 防止号码超长度限制，Django其实会自动截取前11个char
            raise Http404

        try:
            user_obj = User.objects.get(pk=user_id)
        except:
            raise Http404
        else:
            user_obj.profile.phone = phone
            print "change: {}".format(user_obj.profile.phone)
            # user_obj.save() # phone在profile中，直接save user_obj 不生效
            user_obj.profile.save()
            print "saved!!!!"

        return redirect("/user/userlist")