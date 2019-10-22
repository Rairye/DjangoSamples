from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from . import QABot


def home (request):
	response = {'response': None}
	return render(request, 'qabot_manager/qabot.html', response)
# Create your views here.

@ensure_csrf_cookie
def getanswer(request):
	input = request.POST.get('question')
	result = QABot.get_response(input) if len(input) > 0 else "Please input a question, and try again."
	response = {'response' : result}
	print(response)
	return render(request, 'qabot_manager/qabot.html', response)