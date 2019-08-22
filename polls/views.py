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
    entry: dict = {}
    if request.method == 'POST':
        data = request.POST
        fiction_result = Fiction.objects.create(title=data['title'],
                                                author=data['author'],
                                                last_update_time=data['last_update_time'],
                                                desc=data['desc'],
                                                status=data['status'],
                                                convert=data['convert'],
                                                latest_chapter=data['latest_chapter'],
                                                class_id=data['class_id'])
        entry = {'status': 'success', 'msg': '操作成功', 'id': fiction_result.pk}

    else:
        entry = {'status': 'fail', 'msg': '请求方式有误'}

    return JsonResponse(entry, status=201)


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
    result = {'status': '', 'msg': ''}
    if request.method == 'POST':
        data = request.POST  # 获取所有的数据
    else:
        result['status'] = 'fail'; request['msg'] = '操作失败'

    return JsonResponse(result, status=201)
