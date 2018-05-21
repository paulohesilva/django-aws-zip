# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_aws_zip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='log',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='task',
            name='key',
            field=models.CharField(null=True, blank=True, max_length=5000),
        ),
    ]
