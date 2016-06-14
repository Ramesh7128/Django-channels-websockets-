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

	# def save(self, *args, **kwargs):
	# 	"""
	# 	Hooking send_notification into the save of the object as I'm not
	# 	the biggest fan of signals.
	# 	"""
	# 	result = super(Calculations, self).save(*args, **kwargs)

	# 	if s['query_list']:
	# 		q = s['query_list']
	# 	else:
	# 		q = [] 
	# 	q = s['query_list']
	# 	q.append(self.calcEntries)


	# 	if len(q) == 10:
	# 		q.pop(0)
	
	# 	s['query_list'] = q 
	# 	t= json.dumps(q)

	# 	print q


		# notification = {
		# "query": t,
		# }
		# Encode and send that message to the whole channels Group for our
	# 	# liveblog. Note how you can send to a channel or Group from any part
	# 	# of Django, not just inside a consumer.
	# 	Group("calculations").send({
	# 	# WebSocket text frame, with JSON content
	# 	"text": json.dumps(notification),
	# 	})
	# 	return result

	def __unicode__(self):
		if self.user:
			return self.user
		else:
			return self.calcEntries


			