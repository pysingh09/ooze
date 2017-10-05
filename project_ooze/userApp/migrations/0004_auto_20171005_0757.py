# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_auto_20171005_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_password_reset_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]