from django.shortcuts import render
# Create your views here.
from calcapp.models import Calculations

def querySave(request):

	if request.method == 'POST':
		queryString = request.POST.get('query_value')
		calcQuery = Calculations.objects.create(calcEntries=queryString)
		return  render(request,'index.html')

	return  render(request, 'index.html')
