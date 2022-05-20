from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=600)

class Comment(models.Model):
    user_comm = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
