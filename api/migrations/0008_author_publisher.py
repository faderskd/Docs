# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20150704_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ForeignKey(to='api.Publisher', default=100),
            preserve_default=False,
        ),
    ]
