from django.shortcuts import render


def add(request):
    if request.method == "GET":
        return render(request, "goods/add.html", {})
    else:
        pass
