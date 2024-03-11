from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    author = models.CharField(max_length=30, blank=False, null=False)
    year = models.IntegerField()

    def __str__(self):
        return self.title
     



