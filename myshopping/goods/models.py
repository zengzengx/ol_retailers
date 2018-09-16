from django.db import models

import store


class GoodsType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="商品类型")
    cover = models.ImageField(upload_to="static/images/goods", default="static/images/goods/default.jpg", verbose_name="商品类型图片")
    intro = models.TextField(verbose_name="商品类别描述")
    parentType = models.ForeignKey('self', null=True, blank=True, verbose_name="父级类型", on_delete=models.CASCADE)


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="商品名称")
    # price = models.DecimalField(max_digits=6, decimal_places=2)  # 第一个表示共有几位，第二个表示小数点后面有几位
    price = models.FloatField(verbose_name="商品价格")
    stock = models.IntegerField(verbose_name="商品库存")
    count = models.IntegerField(default=0, verbose_name="销售数量")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="上架时间")
    intro = models.TextField(verbose_name="商品描述")
    store = models.ForeignKey(store.models.Store, on_delete=models.CASCADE)


class GoodsImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to="static/images/goods", default="static/images/goods/default.jpg", verbose_name="商品图片")
    intro = models.TextField(verbose_name="商品描述", null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name="是否默认显示该图片")

