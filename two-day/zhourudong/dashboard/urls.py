#!/usr/bin/env python
#-- coding: utf-8 --
#Time: 2017/3/14 11:29
#Author: zhourudong

from django.conf.urls import include, url
from . import views
from . import user

urlpatterns = [

    url(r'^login/', views.LoginView.as_view()),
    url(r'^logout/', views.LogoutView.as_view()),
    url(r'^$', views.IndexView.as_view()),

    url(r'^user/',include([
        url(r'^userlist/$', user.UserListView.as_view()),
        url(r'^modifystatus/$', user.ModifyUserStatusView.as_view()),
    ])),

]