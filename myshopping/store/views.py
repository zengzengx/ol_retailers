from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from . import models


@login_required
def add(request):
    if request.method == "GET":
        return render(request, "store/add.html", {})
    else:
        try:
            name = request.POST["name"]
        except:
            return render(request, "store/add.html", {"msg": "店铺名称不能为空"})
        intro = request.POST.get("intro")
        if intro == "":
            intro = "这个人很懒什么也没描述"
        try:
            cover = request.FILES["cover"]
            store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
        except:
            store = models.Store(name=name, intro=intro, user=request.user)
        store.save()
        return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


@require_GET
def list(request):
    stores = models.Store.objects.filter(user=request.user, status__in=[0, 1])
    return render(request, "store/list.html", {"stores": stores})


@login_required
def update(request, s_id):
    store = models.Store.objects.get(pk=s_id)
    if request.method == "GET":
        return render(request, "store/update.html", {"store": store})
    else:
        try:
            name = request.POST["name"]
        except:
            return render(request, "store/add.html", {"msg": "店铺名称不能为空"})
        intro = request.POST.get("intro")
        if intro == "":
            intro = "这个人很懒什么也没描述"
        try:
            cover = request.FILES["cover"]
            store.name = name
            store.intro = intro
            store.cover = cover
        except:
            store.name = name
            store.intro = intro
        store.save()
        return render(request, "store/detail.html", {"msg": "修改成功", "store": store})


@require_GET
def change_stu(request, s_id, status):
    store = models.Store.objects.get(pk=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("store:list"))
    else:
        return render(request, "store/detail.html", {"store": store})


@login_required
def detail(request, s_id):
    store = models.Store.objects.get(pk=s_id)
    return render(request, "store/detail.html", {"store": store})

