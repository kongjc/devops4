# coding:utf8
from django.views.generic import TemplateView,View,ListView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth import authenticate,login,logout       #导入模块：用户认证，登录，登出；
from django.http import HttpResponse,JsonResponse, Http404               #导入模块：HttpResponse,JsonResponse
from dashboard.models import Department


'''用户列表“模版”函数视图

class UserListView(TemplateView):
    template_name = "user/userlist.html"
    before_index = 5
    after_index = 4

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        userlist = User.objects.all()           #获取所有的用户列表对象
        paginator = Paginator(userlist, 5)     #实例化Paginator
        page = self.request.GET.get("page", 1)  #获取当前第几页（页码数）
        # print dir(paginator)
        # print paginator.num_pages           # 总页数
        # print paginator.count               # 总行数
        # print paginator.object_list         # 用户列表
        # print paginator.page_range          # 返回总分页列表：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # print paginator.per_page            # 页面显示行数

        try:
            page_obj = paginator.page(page)      #获取当前页的数据
            # print page_obj.has_next()           # 有下一页返回True
            # print page_obj.has_previous()       # 有上一页返回True
            # print page_obj.previous_page_number()  # 返回上一页的页码，不存在抛出异常
            # print page_obj.next_page_number()   # 返回下一页的页码，不存在抛出异常
            # print page_obj.start_index()
            # print page_obj.object_list
            # print page_obj.number
        except EmptyPage:
            page_obj = paginator.page(1)         #如果出错，设置默认页

        start_index = page_obj.number - self.before_index
        if start_index < 0 :
            start_index = 0
        end_index = page_obj.number + self.after_index

        print page_obj.paginator.page_range[start_index: end_index]
        page_range = page_obj.paginator.page_range[start_index: end_index]
        context['page_range']= page_range
        context["page_obj"] = page_obj
        return context

    def get(self, request, *args, **kwargs):
        self.request = request
        return super(UserListView,self).get(request, *args, **kwargs)
'''


'''用户列表“列表”函数视图
'''
class UserListView(ListView):
    template_name = "user/userlist.html"
    model = User
    paginate_by = 10
    before_index = 5
    after_index = 4

    # print dir(ListView)
    # 思路：
    #     1、需要答打印userlist；
    #     2、需要知道当前第几页
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        page_obj = context['page_obj']
        context['page_range'] = self.get_page_range(page_obj)
        return context

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        end_index = page_obj.number + self.after_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: end_index]


'''修改用户信息函数视图
'''
class ModifyUserStatusView(View):
    def post(self, request):
        ret = {"status": 0}
        user_id = request.POST.get('user_id', None)
        try:
            user = User.objects.get(pk=user_id)         #pk可以理解为id
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except User.DoesNotExist:
            print 'ERROR: 上面执行有错误'
            ret['status'] = 1
            ret['errmsg'] = "用户不存在"
        return JsonResponse(ret, safe=True)


'''修改用户部门信息函数视图
'''
class ModifyDepartmentView(TemplateView):
    template_name = "user/modify_department.html"

    '''渲染html页面'''
    def get_context_data(self, **kwargs):
        context = super(ModifyDepartmentView, self).get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        context["user_obj"] = User.objects.get(pk=self.request.GET.get('user', None))
        return context

    '''处理HTML页面提交的POST数据'''
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
        return redirect("/user/list/")

    '''定义request方法'''
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyDepartmentView, self).get(request, *args, **kwargs)



'''修改用户手机信息函数视图
'''
class ModifyPhoneView(TemplateView):
    template_name = "user/modify_phone.html"

    '''渲染html页面'''
    def get_context_data(self, **kwargs):
        context = super(ModifyPhoneView, self).get_context_data(**kwargs)
        context["user_obj"] = User.objects.get(pk=self.request.GET.get('user', None))
        return context

    '''处理HTML页面提交的POST数据'''
    def post(self, request):
        # 获取提交的数据
        user_id = request.POST.get('id', None)
        user_phone = request.POST.get('phone', None)
        # 判断是否非法，“否”则返回标准404页面
        if not user_id or not user_phone:
            raise Http404
        try:
            user_obj = User.objects.get(pk=user_id)
        except: # 有任何异常都抛出404错误
            raise Http404
        else:
            # 执行修改动作
            user_obj.profile.phone = user_phone
            user_obj.profile.save()
        # 返回到页面
        return redirect("/user/list/")

    '''定义request方法'''
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(ModifyPhoneView, self).get(request, *args, **kwargs)


'''用户登录函数视图
'''
class UserLoginView(TemplateView):
    template_name = "user/login.html"

    def post(self, request):
        if request.method == "GET":
            return render(request,{"title":"MoXiu 运维平台"})
        elif request.method == "POST":
            ret = {"status": 0}
            username = request.POST.get("username",None)
            password = request.POST.get("password",None)
            # 验证用户名和密码
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    ret['next_url'] = "/"
                else:
                    ret['status'] = 1
                    ret['errmsg'] = "用户被禁用"
            else:
                ret['status'] = 2
                ret['errmsg'] = "用户名或密码错误"
            return JsonResponse(ret, safe=True)


'''用户登出函数视图
'''
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/user/login/")


