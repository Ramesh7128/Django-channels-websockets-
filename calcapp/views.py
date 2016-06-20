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
		return  render(request,'index.html')
		
	if "no_of_entries" in request.session:
		cal = Calculations.objects.latest('id')
		print cal.id, "dskndfkjnskfnskdfnskndf"
		entries = int(cal.id) - int(request.session['no_of_entries'])
		print entries, "dksdkjsfkns"
		if int(entries) > 10:
			entries = 10
		calcEntries =  Calculations.objects.order_by('-timestamp')[:entries]
		context_dict['queries'] = calcEntries
	else:
		cal = Calculations.objects.latest('id')
		request.session['no_of_entries'] = cal.id
	return  render(request, 'index.html', context_dict)
