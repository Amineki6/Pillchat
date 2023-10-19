from django.shortcuts import render
from django.urls import reverse
from func import process_message
from django.http import JsonResponse


import json




# Create your views here.

def convers(request, title):
	r = []
	for s in title.split('['):
		r += s.split(']')

	content = {'title':r[0], 'company':r[1], 'fulltitle': title}
	return render(request, 'conversation.html', content)



def message_endpoint(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		message = data.get('message')
		title = data.get('title')
		sent = data.get('sent')
		response = process_message(message, title)
		return JsonResponse({'response': response})