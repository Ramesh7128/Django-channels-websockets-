from django.shortcuts import render
# Create your views here.
from calcapp.models import Calculations
from channels import Group
import json

def querySave(request):

	if request.method == 'POST':
		queryString = request.POST.get('query_value')
		calcQuery = Calculations.objects.create(calcEntries=queryString)
		if 'query_list' in request.session:
			q = request.session['query_list']
		else:
			q= []

		q.append(queryString)
		if len(q)== 10:
			q.pop(0)

		request.session['query_list'] = q

		notification = {
	 	"query": q,
	 	}

		Group("calculations").send({
		# WebSocket text frame, with JSON content
		"text": json.dumps(notification),
		})


		return  render(request,'index.html')

	return  render(request, 'index.html')
