# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('geo_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoinfo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 13, 52, 10, 435133, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
