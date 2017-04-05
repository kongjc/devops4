#!/usr/bin/env python
#-*- coding:utf8 -*-
from django.conf.urls import url ,include

from dashborad import  views
from dashborad import  user

urlpatterns = [
    url(r'^user/login/$', views.login_view),
    url(r'^$', views.IndexView.as_view()),
    #url(r'^user/userlist/$',user.UserListView.as_view()),
    url(r'^user/',include([
        #url(r'^userlist/$',user.UserListView.as_view()),
        url(r'^userlist/$',user.USERLISTVIEW.as_view()),
        url(r'^modifystatus/$',user.ModifyUserStatusView.as_view()),
        url(r'^modifydepartment/$',user.ModifyDepartmentView.as_view()),
        url(r'^modifyphone/$',user.ModifyPhoneView.as_view()),
    ]
    ))
]