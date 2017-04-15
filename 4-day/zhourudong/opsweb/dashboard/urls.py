# coding:utf8
from django.conf.urls import include, url
from . import views
from dashboard import user
from dashboard.user import group

urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^$', views.IndexView.as_view()),
    url(r'permission/', include([
        # 无权操作的页面
        url(r'none/$', views.permission),
    ])),

    url(r'^user/', include([
        # 用户列表页
        url(r'^userlist/$', user.UserListView.as_view()),
        # 修改用户状态  开启 禁用
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view()),
        url(r'^modifydepartment/$', user.ModifyDepartmentView.as_view(), name='modifydepartment'),
        # 修改用户手机号码
        url(r'^modifyuserphone/', user.ModifyUserPhoneView.as_view(), name='modify_user_phone'),
    ])),
    # 组
    url(r'^group/', include([
        #  获取用户组信息
        url(r'^$', group.GroupView.as_view()),
        # 组列表
        url(r'^list/$', group.GroupListView.as_view(), name='group_list'),
        # 用户 添加到 组显示下拉框内容
        url(r'^usergroup/$', group.UserGroupView.as_view()),
        # 权限列表
        url(r'^permission/$', group.GroupPermissionListViwe.as_view(), name='group_permission'),
    ])),
]
