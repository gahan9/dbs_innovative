from django.db import models


class Title(models.Model):
    title_id = models.CharField(max_length=16)
    ordering = models.IntegerField()
    title = models.CharField(max_length=512)
    region = models.CharField(max_length=8, null=True, blank=True)
    language = models.CharField(max_length=16, null=True, blank=True)
    types = models.CharField(max_length=32, null=True, blank=True)
    attributes = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_original_title = models.BooleanField(null=True, blank=True)
