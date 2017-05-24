# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    
    sender = models.CharField(max_length = 13)
    receiver = models.CharField(max_length = 13) 
    raw = models.CharField(max_length = 200)
    timestamp = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.sender
