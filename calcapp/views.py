from django.shortcuts import render
# Create your views here.
from calcapp.models import Calculations
from channels import Group
import json
from channels.sessions import channel_session
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def querySave(request):
	context_dict = {}
	if request.method == 'POST':
		queryString = request.POST.get('query_value')
		calcQuery = Calculations.objects.create(calcEntries=queryString)
		if 'no_of_visits' in request.session:
			request.session['no_of_visits'] += 1
		else:
			request.session['no_of_visits'] = 1
		return  render(request,'index.html')
	if "no_of_visits" in request.session:
		entries = request.session['no_of_visits']
		if int(entries) > 10:
			entries = 10
		calcEntries =  Calculations.objects.order_by('-timestamp')[:entries]
		context_dict['queries'] = calcEntries
	else:
		pass
	return  render(request, 'index.html', context_dict)
