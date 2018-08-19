# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_profile.models import User

from django.db import models
class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True) 

# Create your models here.
