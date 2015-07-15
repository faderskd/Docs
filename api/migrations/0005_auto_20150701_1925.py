# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from pygments.formatters import _automodule


def copy_publishers(apps, schema_editor):
    Author = apps.get_model("api", "Author")
    for author in Author.objects.all():
        books = author.book_set.all()
        for book in books:
            book.publisher = author.publisher
            book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150701_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, to='api.Publisher'),
            preserve_default=False,
        ),
        migrations.RunPython(copy_publishers)
        ,
        migrations.RemoveField(
            model_name='author',
            name='publisher',
        ),
    ]
