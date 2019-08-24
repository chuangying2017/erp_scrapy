from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from polls.models import FictionClass, Fiction, FictionChapter
import time
from pymysql import MySQLError


# Create your views here.


def index(request):
    data = {"status": "1", "msg": "success"}
    j = json.dumps(data)
    return HttpResponse(j, status=201)


''' 小说创建 '''


def fiction(request):
    if request.method == 'POST':
        data = request.POST
        # res = Fiction.objects.filter(title=data['title'])
        # if res.exists():
        #     fiction_result = res.first()
        #     msg = 'already'
        # else:
        fiction_result = Fiction.objects.create(title=data['title'],
                                                author=data['author'],
                                                last_update_time=data['last_update_time'],
                                                desc=data['desc'],
                                                status=data['status'],
                                                latest_chapter=data['latest_chapter'],
                                                class_id=data['class_id'])
        msg = 'create success'

        entry = {'status': 'success', 'msg': msg, 'id': fiction_result.pk}
    else:
        entry = {'status': 'fail', 'msg': 'request mode mistaken'}
    """:return table id"""
    return JsonResponse(entry, status=201)


'''
小说分类
'''


def fiction_class(request):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if request.method == 'POST':
        # some_queryset = FictionClass.objects.filter(title__exact=request.POST['title'])
        # if some_queryset.exists():
        #     first = some_queryset.first()
        #     entry = first.title
        #     data = first.pk
        # else:
        #     res = FictionClass.objects.create(title=request.POST['title'], create_time=now_time, update_time=now_time)
        #     entry = res.title
        #     data = res.pk
        res = FictionClass.objects.create(title=request.POST['title'], create_time=now_time, update_time=now_time)
        entry = res.title
        data = res.pk
        entry = {'msg': entry, 'id': data}
    else:
        return JsonResponse({'status': 'fail', 'msg': 'method is not use!'})

    return JsonResponse(entry)


'''
小说章节
'''


def fiction_chapter(request):
    result = {'status': '', 'msg': ''}
    if request.method == 'POST':
        data = request.POST  # 获取所有的数据
        try:
            # res = FictionChapter.objects.filter(chapter=data['chapter'])
            # result['status'] = 'success'
            # if res.exists():
            #     result['msg'] = 'already'
            # else:
            #     res.create(fiction_id=data['fiction_id'], chapter=data['chapter'],
            #                title=data['title'],
            #                content=data['content'])
            #     result['msg'] = 'insert success'
            # fiction_list_to_insert: list = []

            FictionChapter.objects.create(fiction_id=data['fiction_id'],
                                          title=data['title'],
                                          content=data['content'])

            result['msg'] = 'insert success'

        except ConnectionError:
            result['status'] = 'fail'
            result['msg'] = 'database connect fail'
        except MySQLError:
            result['status'] = 'fail'
            result['msg'] = 'mysql error'
        except MemoryError:
            result['status'] = 'fail'
            result['msg'] = 'memory piss'
    else:
        result['status'] = 'fail'
        request['msg'] = 'operation fail'

    return JsonResponse(result, status=201)
