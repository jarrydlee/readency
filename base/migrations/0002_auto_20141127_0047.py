# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('service_item_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(to='base.Profile')),
                ('service', models.ForeignKey(to='base.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 11, 27, 0, 47, 8, 186289, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2014, 11, 27, 0, 47, 16, 674211, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 11, 27, 0, 47, 38, 108120, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2014, 11, 27, 0, 47, 41, 866843, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceconnection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 11, 27, 0, 47, 44, 235014, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceconnection',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2014, 11, 27, 0, 47, 45, 410945, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
