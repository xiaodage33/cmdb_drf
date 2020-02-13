from django.db import models


class Server(models.Model):
    """
    服务器表
    """
    hostname = models.CharField(verbose_name="主机名",max_length=32)
    last_date = models.DateField(verbose_name='最近汇报时间',null=True,blank=True)

#
# class Disk(models.Model):
#     """
#     硬盘表
#     """
#     slot = models.CharField(verbose_name='槽位',max_length=32)
#     pd_type = models.CharField(verbose_name='类型',max_length=32)
#     capacity = models.CharField(verbose_name='容量',max_length=32)
#     model = models.CharField(verbose_name='型号',max_length=32)
#     server = models.ForeignKey(verbose_name='服务器',to='Server',on_delete=False)
#
# class AssetsRecord(models.Model):
#     """
#     资产变更记录
#     """
#     content = models.TextField(verbose_name='内容')
#     server = models.ForeignKey(verbose_name='服务器',to='Server',on_delete=False)
#     create_date = models.DateTimeField(verbose_name='时间',auto_now_add=True)











