from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from channels import Group
import json


# Create your models here.


class Calculations(models.Model):

	calcEntries = models.CharField(max_length=200, blank=False,null=False)
	user = models.ForeignKey(User, blank=True, null=True)

	def save(self, *args, **kwargs):
		"""
		Hooking send_notification into the save of the object as I'm not
		the biggest fan of signals.
		"""
		result = super(Calculations, self).save(*args, **kwargs)

		notification = {
		"query": self.calcEntries,
		}
		# Encode and send that message to the whole channels Group for our
		# liveblog. Note how you can send to a channel or Group from any part
		# of Django, not just inside a consumer.
		Group("calculations").send({
		# WebSocket text frame, with JSON content
		"text": json.dumps(notification),
		})
		return result

	def __unicode__(self):
		if self.user:
			return self.user
		else:
			return self.calcEntries


			