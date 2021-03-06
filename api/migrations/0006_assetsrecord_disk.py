# Generated by Django 3.0.3 on 2020-02-13 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200213_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='槽位')),
                ('pd_type', models.CharField(max_length=32, verbose_name='类型')),
                ('capacity', models.CharField(max_length=32, verbose_name='容量')),
                ('model', models.CharField(max_length=32, verbose_name='型号')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server', verbose_name='服务器')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server', verbose_name='服务器')),
            ],
        ),
    ]
