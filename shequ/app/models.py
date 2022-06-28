from django.db import models


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    phone = models.IntegerField()


class Resource(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=64)
    author = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
# User.objects.create(name="awfj",password="12345",phone=23456)


class nocheck(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=64)
    author = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)


# 博客
class Blog(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=64)
    author = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    thumb_up = models.BigIntegerField(default=0, null=False)
    comment = models.BigIntegerField(default=0,null=False)
    star = models.BigIntegerField(default=0,null=False)


# 笔记
class note(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=64)
    author = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# index App models.py

from django.db import models
from django.utils import timezone


# 文件模型
class FileModel(models.Model):
    # 文件名称
    name = models.CharField(max_length=50)
    # 文件保存路径
    path = models.CharField(max_length=100)
    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)