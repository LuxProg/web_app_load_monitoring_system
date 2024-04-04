from django.db import models

# Create your models here.


class Dip_work(models.Model):
    title = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    content = models.TextField(max_length=10000, blank=True)
    writer = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
