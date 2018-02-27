# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
