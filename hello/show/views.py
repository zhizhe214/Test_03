from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

"""
     django.http 模块中定义了 HttpResponse 对象的API
     作用：不需要调用模板直接返回数据
     HttpResponse属性：
     content: 返回内容，字符串类型
     charset: 响应的编码字符集
     status_code: HTTP 响应的状态码
"""


def hello(request):
    return HttpResponse('Hello World !')


def msg(request, name, age):
    return HttpResponse('My name is' + name + ',<br/>i am ' + age + ' years old .')
