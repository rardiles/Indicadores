# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0009_auto_20160310_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
