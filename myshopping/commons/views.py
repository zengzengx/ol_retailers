from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse

from . import utils


def index(request):
    return render(request, "index.html", {})


def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, code = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    request.session['check_code'] = code
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())
