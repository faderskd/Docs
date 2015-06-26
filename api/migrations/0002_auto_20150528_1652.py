# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='headshot',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
    ]
