from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from . import ChatBot

chat_history = []


def home (request):
	global postable
	random_sent = ChatBot.get_random()
	chat_history.append("<span style = \"font-style: italic\"> - Bot: " + random_sent + "</span>")
	response = {"chat_history" : chat_history}
	return render(request, 'chatbot_manager/bot.html', response)

@ensure_csrf_cookie
def postresponse(request):
	global chat_history
	input = request.POST.get('input')
	chat_history.append("- User: " + input)
	response = {"chat_history" : chat_history}
	return render(request, 'chatbot_manager/bot.html', response)
		
@ensure_csrf_cookie
def getresponse(request):
	postresponse(request)
	global postable
	postable = True
	input = request.POST.get('input')
	global chat_history
	chat_response = ChatBot.get_response(input)
	chat_history.append("<span style = \"font-style: italic\"> - Bot: " + chat_response + "</span>")
	response = {"chat_history" : chat_history}
	return render(request, 'chatbot_manager/bot.html', response)
