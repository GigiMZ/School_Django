from django.db import models

class Library(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=20)
    description = models.TextField(default="", max_length=100)
    view_count = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)