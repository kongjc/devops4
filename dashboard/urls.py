#!/usr/bin/python
# coding=utf-8

"""opsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from dashboard import views
from dashboard import user
from dashboard.user import group


urlpatterns = [

    url(r'^$', views.IndexView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),

    url(r'^user/', include([
        url(r'^list/$', user.UserListView.as_view()),
        url(r'^modifystatus/$', user.ModifyUserStatus.as_view()),
        url(r'^modifydepartment/$', user.ModifyDepartmentView.as_view()),
        # url(r'^modifyphone/$', user.ModifyPhoneViewTmp.as_view()),
        url(r'^modifyphone/$', user.ModifyPhoneView.as_view()),

        url(r'^modifycnname/$', user.ModifyCNnameViewTmp.as_view()),
    ])),

    url(r'^permission/', include([
        url(r'^none/$', views.permission),
    ])),

    url(r'^group/', include([
        url(r'^$', group.GroupView.as_view()),
        url(r'^list/$', group.GroupListView.as_view()),
        url(r'^usergroup/$', group.UserGroupView.as_view()),
        url(r'^permission/$', group.GroupPermissionListView.as_view()),
    ])),

]
