# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150701_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='foo',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
