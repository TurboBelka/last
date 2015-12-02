# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_info', '0002_geoinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoinfo',
            name='user_agent',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
