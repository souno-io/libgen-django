from django.db import models
from django.utils import timezone

# Create your models here.


class SysConfigs(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    web_name = models.CharField('系统名字', max_length=200, null='Flase', help_text='用于系统各处的logo显示')
    web_desc = models.CharField('系统描述', max_length=200, null='Flase', help_text='主页下方的副标题')
    web_foot = models.CharField('系统页尾', max_length=200, null='Flase', help_text='整个系统目标页尾说明')
    server_ip = models.CharField('存储服务器IP', max_length=20,  null='Flase', help_text='用于存储和配置服务器地址')
    server_port = models.CharField('存储服务器端口', max_length=20,  null='Flase', help_text='用于存储和配置服务器端口')
    addeddatetime = models.TextField('创建时间', help_text='添加时间', default=timezone.now)

    class Meta:
        verbose_name = u"系统设置"
        verbose_name_plural = verbose_name