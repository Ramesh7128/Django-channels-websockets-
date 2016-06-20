from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session, http_session_user, channel_session_user, channel_session_user_from_http
from calcapp.models import Calculations
import json
from django.core import serializers
from channels.auth import http_session_user
from django.contrib.sessions.backends.db import SessionStore

# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Add them to the right group
    Group("calculations").add(message.reply_channel)

@channel_session_user
def ws_receive(message):
	print message.user, "dksjbkjsbd"
	# if "no_of_visits" in message.http_session:
	# 	message.http_session['no_of_visits'] += 1
	# else:
	# 	message.http_session['no_of_visits'] = 1
	# print message.http_session['no_of_visits']
	data = json.loads(message['text'])
	Group('calculations').send({"text": json.dumps(data)})

# Connected to websocket.receive
# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("calculations").discard(message.reply_channel)