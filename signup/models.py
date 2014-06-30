from django.db import models

# Create your models here.

class Registration(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    commit = models.IntegerField()

    def __unicode__(self):
        return self.username