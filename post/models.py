from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=40)
    like_count = models.IntegerField()
    published = models.BooleanField()
    