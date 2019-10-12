from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
