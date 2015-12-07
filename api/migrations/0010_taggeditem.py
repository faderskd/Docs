# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0009_bookimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('tag', models.SlugField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
    ]
