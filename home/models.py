from django.db import models
from django.db.models.fields import CharField, TextField
from acc.models import User


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    ctime = models.DateTimeField()
    up = models.ManyToManyField(User, blank=True) #User와 Board가 N:N 관계



    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) >= 20:
            return self.content[:20]+'...'
        return self.content

class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete = models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
