from django.db import models
from django.urls import reverse


class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField()
    course = models.CharField()

    def get_absolute_url(self):
        return reverse("thanks") #redirect to thanks template
