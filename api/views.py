import json
import datetime

from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api import models
from api.service.disk import process_disk_info

@method_decorator(csrf_exempt,name='dispatch')
class ServerView(View):

    def get(self,request,*args,**kwargs):
        today = datetime.date.today()
        # 最近汇报时间小于今天 or 最近汇报时间
        """
        con = Q()
        con.connector = 'OR'
        con.children.append(('last_date__lt', today))
        con.children.append(('last_date__isnull', True))
        server_list = models.Server.objects.filter(con)
        """

        server_queryset = models.Server.objects.filter(Q(last_date__lt=today) | Q(last_date__isnull=True)).values_list(
            'hostname')
        server_list = [item[0] for item in server_queryset]
        print(server_list)
        return JsonResponse({'status': True, 'data': server_list})

    def post(self,request,*args,**kwargs):
        content = request.body.decode('utf-8')
        server_info_dict = json.loads(content)
        hostname = server_info_dict['host']
        info_dict = server_info_dict['info']

        host_object = models.Server.objects.filter(hostname=hostname).first()
        if not host_object:
            print('服务器不存在')
            return HttpResponse('服务器不存在')
        process_disk_info(host_object, info_dict['disk'])

        host_object.last_date = datetime.date.today()
        host_object.save()
        # 获取数据之后，把他们放到数据库
        return HttpResponse('成功')