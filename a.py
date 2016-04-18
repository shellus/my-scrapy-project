# coding=utf-8
import sys
import os

sys.path.append('C:\Users\shellus\www\python\mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

if __name__ == "__main__":
    from learn.models import Article
    Article.objects.create(title="我爱易", link="n", content="c")


