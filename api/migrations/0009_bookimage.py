# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_author_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('book', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
