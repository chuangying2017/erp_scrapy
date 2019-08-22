from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
import json
from polls.models import FictionClass, Fiction, FictionChapter
import time


# Create your views here.


def index(request):
    data = {"status": "1", "msg": "success"}
    j = json.dumps(data)
    return HttpResponse(j, status=201)


''' 小说创建 '''


def fiction(request):
    pass


'''
小说分类
'''


def fiction_class(request):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if request.method == 'POST':
        some_queryset = FictionClass.objects.filter(title__exact=request.POST['title'])
        if some_queryset.exists():
            first = some_queryset.first()
            entry = first.title
            data = first.pk
        else:
            res = FictionClass.objects.create(title=request.POST['title'], create_time=now_time, update_time=now_time)
            entry = res.title
            data = res.pk
        entry = {'msg': entry, 'id': data}
    else:
        return JsonResponse({'status': 'fail', 'msg': '方法不可用'})

    return JsonResponse(entry)


'''
小说章节
'''


def fiction_chapter(request):
    pass
