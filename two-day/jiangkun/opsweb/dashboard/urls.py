from django.conf.urls import include, url
from . import views
# from dashboard import user
from . import user

urlpatterns = [
    url(r'^hello/$', views.hello),
    # url(r'^login/$', views.login_view),
    url(r'^login/$', views.LoginView.as_view()),
    # url(r'^logout/$', views.logout_view),
    url(r'^logout/$', views.LogoutView.as_view()),
    # url(r'^test_form/$', views.test_form),
    url(r'^$', views.IndexView.as_view()),

    # url(r'^user/userlist/$', user.UserListView.as_view())
    url(r'^user/', include([
        url(r'list/$', user.UserListView.as_view()),
        url(r'modifystatus/$', user.ModifyUserStatusView.as_view())
    ]))
]
