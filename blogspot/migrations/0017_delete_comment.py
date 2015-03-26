# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogspot', '0016_auto_20150227_0117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
