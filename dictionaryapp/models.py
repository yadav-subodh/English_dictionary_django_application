from django.db import models

# Create your models here.
"""
Defines model for Dictionary table to store, retrieve, update the data
Models are blueprint of tables
"""


class Dictionary(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=200)
    synonyms = models.CharField(max_length=200)
    antonyms = models.CharField(max_length=200)
    usage = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True, blank=True)


"""
Defines model for SuperUser table to store, retrieve, update the data
"""


class SuperUser(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)


"""
Defines model for User table to store, retrieve, update the data
"""


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    comments = models.TextField(max_length=200)
