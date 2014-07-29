from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=169)
    Body = models.TextField()
    Link = models.CharField( max_length=200)
    File = models.FileField()
    art_date = models.DateTimeField(auto_now=True)
    group_id = models.ForeignKey(Group)
    Author_id = models.ForeignKey(User)

    def __unicode__(self):
        return self.Title


class Comments(models.Model):
    User_id = models.ForeignKey(User)
    Comment = models.TextField(max_length=200)
    Group_id = models.ForeignKey(Group)
    Article_id = models.ForeignKey(Article)
    com_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.Comment