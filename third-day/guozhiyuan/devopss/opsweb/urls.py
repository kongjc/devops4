#coding=utf8
from django.conf.urls import url
from opsweb.views import IndexView,LogoutView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^logout/$',LogoutView.as_view()),
]