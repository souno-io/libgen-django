from django.shortcuts import render, HttpResponse
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect


def login_view(request):
    return render(request, 'login.html')


def login_check(request):
    username = request.POST.get('name')
    password = request.POST.get('passwd')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        # 验证通过后的代码
        print('登录成功: %s' % user.username)
        login(request, user)
        # request.session.set_expiry(0)
        return HttpResponse('success')
    else:
        # 验证失败后的代码
        print('登录失败 用户名或密码错误')
        return HttpResponse('fail')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
