from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Calculations(models.Model):

	calcEntries = models.CharField(max_length=200, blank=False,null=False)
	user = models.ForeignKey(User, blank=True, null=True)

	def __unicode__(self):
		if self.user:
			return self.user
		else:
			return self.calcEntries


			