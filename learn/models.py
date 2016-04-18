# coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Article(models.Model):
    """文章数据表定义"""
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
