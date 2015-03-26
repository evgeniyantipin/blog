# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogspot', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
