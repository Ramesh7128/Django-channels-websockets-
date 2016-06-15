from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from channels import Group
import json
from django.contrib.sessions.backends.db import SessionStore
s = SessionStore()
from django.utils import timezone


# Create your models here.


class Calculations(models.Model):

	calcEntries = models.CharField(max_length=200, blank=False,null=False)
	user = models.ForeignKey(User, blank=True, null=True)
	timestamp = models.DateTimeField(default=timezone.now, db_index=True)
	
	def __unicode__(self):
		if self.user:
			return self.user
		else:
			return self.calcEntries


			