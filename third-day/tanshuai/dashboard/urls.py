from django.conf.urls import include, url
from . import views
from dashboard import user

urlpatterns = [
    # url(r'^login/$', views.login_view),
    # url(r'^logout/$', views.logout_view),
    url(r'^$', views.IndexView.as_view()),
    url(r'^user/',include([
        url(r'^login/$', user.UserLoginView.as_view()),
        url(r'^logout/$', user.UserLogoutView.as_view()),
        url(r'^list/$',user.UserListView.as_view()),
        url(r'^modifystatus/$',user.ModifyUserStatusView.as_view()),
        url(r'^modifyphone/$',user.ModifyPhoneView.as_view()),
        url(r'^modifydepartment/$',user.ModifyDepartmentView.as_view()),
    ]))
]

