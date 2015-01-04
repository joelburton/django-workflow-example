# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foof', '0002_auto_20150104_0511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moof',
            options={'ordering': ['id']},
        ),
    ]
