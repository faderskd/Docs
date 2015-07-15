# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_book_foo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='foo',
        ),
        migrations.AddField(
            model_name='author',
            name='foo',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
