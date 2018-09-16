

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


from . import models


def user_login(request):
    if request.method == "GET":
        try:
            next_url = request.GET["next"]
        except:
            next_url = ""
        return render(request, "user/user_login.html", {"next_url": next_url})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        code = request.POST["code"]
        next_url = request.POST.get("next")
        # 验证码
        if code != request.session["check_code"]:
            return render(request, "user/user_login.html", {"msg": "验证码错误"})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if next_url == "":
                    next_url = "/user/user_info/"
                # 将用户信息存到request
                login(request, user)
                return redirect(next_url)
            else:
                return render(request, "user/user_login.html", {"msg": "您的账号已被锁定，请联系管理员"})
        else:
            return render(request, "user/user_login.html", {"msg": "账号或密码错误请重新登陆"})


@transaction.atomic
def register(request):
    if request.method == "GET":
        return render(request, "user/register.html", {"msg": "请按要求填写如下内容"})
    elif request.method == "POST":
        username = request.POST["username"]
        nickname = request.POST.get("nickname")
        password = request.POST["password"]
        gender = request.POST.get("gender")
        code = request.POST["code"]
        # 验证码
        if code != request.session["check_code"]:
            return render(request, "user/register.html", {"msg": "验证码错误"})
        try:
            # 判断用户名是否重复
            User.objects.get(username=username)
            return render(request, "user/register.html", {"msg": "用户名已存在", "stat": False})
        except:
            try:
                models.UserOther.objects.get(nickname=nickname)
                return render(request, "user/register.html", {"msg": "用户昵称已存在", "stat": False})
            except:
                # 保存用户信息
                tid = transaction.savepoint()
                user = User.objects.create_user(username=username, password=password)
                userother = models.UserOther(nickname=nickname, gender=gender, user=user)
                user.save()
                userother.save()
                return render(request, "user/user_login.html", {"msg": "注册成功请登录"})


@require_GET
def check_nickname(request):
    nickname = request.GET["nickname"]
    try:
        models.UserOther.objects.get(nickname=nickname)
        return JsonResponse({"msg2": False})
    except:
        return JsonResponse({"msg2": True})


@require_GET
def check_name(request):
    username = request.GET["username"]
    users = User.objects.filter(username=username)
    print(users)
    if len(users) > 0:
        return JsonResponse({"msg1": False})
    else:
        return JsonResponse({"msg1": True})


@login_required
@transaction.atomic
def user_info(request):
    user = User.objects.get(pk=request.user.id)
    user_ = models.UserOther.objects.get(user_id=request.user.id)
    if request.method == "GET":
        return render(request, "user/user_info.html", {})
    elif request.method == "POST":
        path = models.UserOther.objects.get(user_id=request.user.id).header
        header = request.FILES.get("header", path)
        age = request.POST["age"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        try:
            with transaction.atomic():
                user.email = email
                user_.header = header
                user_.age = age
                user_.phone = phone
                user_.gender = gender
                user.save()
                user_.save()
            return redirect(reverse("user:user_info"))
        except:
            pass


@login_required  # 装饰器表示这个方法只有登陆用户才能访问
def user_logout(request):
    logout(request)
    return render(request, "user/user_login.html", {"msg": "退出成功"})


def changepwd(request, u_id):
    user = User.objects.get(pk=u_id)
    if request.method == "GET":
        return render(request, "user/changepwd.html", {"user": user})
    elif request.method == "POST":
        password = request.POST["password"]
        user.set_password(password)
        user.save()
        return render(request, "user/user_login.html", {"msg": "修改成功请重新登陆"})


@require_GET
def checkpwd(request):
    pwd = request.GET["pwd"]
    user = authenticate(username=request.user.username, password=pwd)
    if user is not None:
        return JsonResponse({"msg": True})
    else:
        return JsonResponse({"msg": False})



