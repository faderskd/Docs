# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def copy_publishers(apps, schema_editor):
    Book = apps.get_model("api", "Book")
    for book in Book.objects.all():
        authors = book.authors.all()
        for author in authors:
            author.publisher = book.publisher
            author.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150626_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['salutation']},
        ),
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ForeignKey(to='api.Publisher', default=1),
            preserve_default=False,
        ),
        migrations.RunPython(copy_publishers),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),

    ]
