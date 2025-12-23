from django.db import models


class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField()
    course = models.CharField()
