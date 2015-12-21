# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    foo = models.CharField(max_length=100, null=True)
    publisher = models.ForeignKey(Publisher)

# tutaj dodalem komentarz

    class Meta:
        ordering = ['salutation']


    def __str__(self):              # __unicode__ on Python 2
        return self.name


class BookManager(models.Manager):
    def foo(self):
        return super(BookManager, self).get_queryset().filter(title='nowa')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)

    objects = BookManager()

    def save(self,*args,**kwargs):
        super(Book,self).save(*args, **kwargs)
        print(self.pk)