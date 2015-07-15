from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Docs.settings'
import django
django.setup()

from api.models import Author

@app.task
def create_author():
    a = Author.objects.create(salutation="celery",name="celery",foo="celery")
    a = Author.objects.create(salutation="celery",name="celery",foo="celery")
    return a.pk