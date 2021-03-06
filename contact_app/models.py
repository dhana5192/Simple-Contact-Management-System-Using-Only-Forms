from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=12)
    alt_mobile_no = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name
