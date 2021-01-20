from django.db import models

from datetime import date


class Blog(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.title