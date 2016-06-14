from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from calcapp.models import Calculations
import json
from django.core import serializers
# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Add them to the right group
    Group("calculations").add(message.reply_channel)

@channel_session
def ws_receive(message):
	try:
		print message.channel_session['no_of_entries'], "ksdnkns"
	except:
		pass
	if 'no_of_entries' in message.channel_session:
		message.channel_session['no_of_entries'] += 1
	else:
		message.channel_session['no_of_entries'] = 1
	print message.channel_session['no_of_entries']
	messages = reversed(Calculations.objects.order_by('-timestamp')[:message.channel_session['no_of_entries']])
	for mess in messages:
		print mess.calcEntries
	data = serializers.serialize('json', Calculations.objects.order_by('-timestamp')[:message.channel_session['no_of_entries']])
	print data,"test"
	Group('calculations').send({"text": data})

# Connected to websocket.receive
# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("calculations").discard(message.reply_channel)