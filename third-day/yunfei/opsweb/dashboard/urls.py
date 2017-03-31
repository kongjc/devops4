from django.conf.urls import url, include
from . import views
from . import user

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^user/', include([
        url(r'^list/$', user.UserListView.as_view()),
        url(r'^status/$', user.ModifyUserStatusView.as_view()),
        url(r'^list_new/$', user.UserListNewView.as_view()),
        url(r'^profile/$', user.ModifyProfileView.as_view()),
    ])),
]
