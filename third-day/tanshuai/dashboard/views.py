# coding:utf8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


# Create your views here.


def hello(request):
    #return HttpResponse("<h3>hello worhd!!,你好，世界!!</h3>")
    data = {"name": "Nick", "age": "25"}
    #return HttpResponse(json.dumps(data), content_type="application/json",status=200)
    data_list = [1,2,3]
    return JsonResponse(data_list,safe=False)


class IndexView(View):
    def get(self, requet):
        return render(requet,"public/index.html")
