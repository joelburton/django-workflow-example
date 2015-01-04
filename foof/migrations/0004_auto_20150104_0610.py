# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foof', '0003_auto_20150104_0526'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE watson_searchentry ALTER meta_encoded TYPE jsonb USING meta_encoded::jsonb;
            CREATE INDEX meta_encoded_idx ON watson_searchentry USING gin (meta_encoded);
            CREATE VIEW workflowpublic.watson_searchentry AS
              SELECT * FROM public.watsonsearch_entry WHERE meta_encoded @> '{"published":true}';
            """
        )
    ]
