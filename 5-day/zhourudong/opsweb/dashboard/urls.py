# coding:utf8
from django.conf.urls import include, url
from . import views
from dashboard import user
from dashboard.user import group

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'permission/', include([
        # 无权操作的页面
        url(r'none/$', views.permission, name="no_permission"),
    ])),

    url(r'^user/', include([
        # 用户列表页
        url(r'^userlist/$', user.UserListView.as_view(), name="user_list"),
        # 修改用户状态  开启用户 禁用用户
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view(), name="modify_user_status"),
        # 修改用户部门
        url(r'^modifydepartment/$', user.ModifyDepartmentView.as_view(), name='modifydepartment'),
        # 修改用户手机号码
        url(r'^modifyuserphone/', user.ModifyUserPhoneView.as_view(), name='modify_user_phone'),
    ])),
    # 组
    url(r'^group/', include([
        #  获取用户组信息
        url(r'^$', group.GroupView.as_view(), name='group'),
        # 组列表
        url(r'^list/$', group.GroupListView.as_view(), name='group_list'),
        # 用户 添加到 组显示下拉框内容
        url(r'^usergroup/$', group.UserGroupView.as_view(), name='usergroup'),
        # 全部组权限列表
        url(r'^permissions_list/$', group.GroupPermissionListViwe.as_view(), name='group_permissions'),
        # 一个组的权限
        url(r'^permissions/$', group.GroupPermissionView.as_view(), name='one_group_permission'),
    ])),
]
