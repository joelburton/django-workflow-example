# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('foof', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
        CREATE SCHEMA workflowpublic;
        CREATE VIEW workflowpublic.foof_moof AS SELECT * FROM public.foof_moof WHERE published;
        """)
    ]
