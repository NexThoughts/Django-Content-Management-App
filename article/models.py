from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=169)
    Body = models.TextField()
    Link = models.CharField( max_length=200)
    File = models.FileField()
    #pub_date = models.DateTimeField('date published')
    group_id = models.CharField(max_length=20)
    Author_id = models.ForeignKey(User)

    def __unicode__(self):
        return self.Title