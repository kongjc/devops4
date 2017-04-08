from django.conf.urls import url
from users.views import UserListView,ModifyUserStatusView,UserLogin,ModifyUserInfoView

urlpatterns = [
    url(r'^userlist/', UserListView.as_view()),
    url(r'^usermodify/$',ModifyUserStatusView.as_view()),
    url(r'^modifyuserinfo/$', ModifyUserInfoView.as_view())
    
]