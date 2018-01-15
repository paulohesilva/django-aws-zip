# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('log', models.CharField(null=True, max_length=10000, blank=True)),
                ('key', models.CharField(null=True, max_length=100, blank=True)),
                ('num_file', models.IntegerField(null=True, blank=True)),
                ('percent', models.IntegerField(null=True, blank=True)),
                ('status', models.IntegerField(choices=[(0, 'in progress'), (1, 'done'), (2, 'fail')], default=0)),
            ],
        ),
    ]
