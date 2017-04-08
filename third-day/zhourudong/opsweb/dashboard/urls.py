#coding:utf8
from django.conf.urls import include, url
from . import views
from dashboard import user

urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^$', views.IndexView.as_view()),

    url(r'^user/', include([
        url(r'^userlist/$', user.UserListView.as_view()),
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view()),
        url(r'^modifydepartment/$', user.ModifyDepartmentView.as_view()),
        # 修改用户手机号码
        url(r'^modifyuserphone/', user.ModifyUserPhoneView.as_view(), name='modify_user_phone'),
    ]))
]

