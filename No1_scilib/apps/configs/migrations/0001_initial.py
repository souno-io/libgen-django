# Generated by Django 3.0.5 on 2020-10-27 11:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysConfigs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('web_name', models.CharField(help_text='用于系统各处的logo显示', max_length=200, null='Flase', verbose_name='系统名字')),
                ('server_ip', models.CharField(help_text='用于存储和配置服务器地址', max_length=20, null='Flase', verbose_name='存储服务器IP')),
                ('server_port', models.CharField(help_text='用于存储和配置服务器端口', max_length=20, null='Flase', verbose_name='存储服务器端口')),
                ('addeddatetime', models.TextField(default=django.utils.timezone.now, help_text='添加时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '系统设置',
                'verbose_name_plural': '系统设置',
            },
        ),
    ]
