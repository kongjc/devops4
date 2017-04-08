#coding=utf8
from django.shortcuts import render
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.



class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html')