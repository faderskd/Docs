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

zmiana poczatkowa na serwerze (najnowsza)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

stan poczatkowy bloku nieruszanego sie zmienil 

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['salutation']

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
