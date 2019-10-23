from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from . import GameManager

score = 0
currentQuestion = 1
question = ""
correct_answer = ""
result = ""
manager = None
refreshable = True

def home (request):
	response = {'response': "Katakana Words", currentQuestion: None}
	return render(request, 'katakanawords_manager/game.html', response)

@ensure_csrf_cookie
def startnew(request):
	global refreshable
	global score
	global currentQuestion
	refreshable = False
	global manager
	manager = GameManager.game()
	score = 0
	currentQuestion = 1
	questiontemp = manager.get_next_question()
	global question
	question = questiontemp[0]
	global correct_answer
	correct_answer = questiontemp[1]
	response = {'response' : question, 'currentQuestion' : currentQuestion}
	return render(request, 'katakanawords_manager/game.html', response)
	
@ensure_csrf_cookie
def getnextquestion(request):
	global refreshable
	global question
	global correct_answer
	global result
	global currentQuestion
	result = ""
	if refreshable == True:
		questiontemp = manager.get_next_question()
		question = questiontemp[0]
		correct_answer = questiontemp[1]
		refreshable = False
		currentQuestion +=1
	response = {'response' : question, 'currentQuestion' : currentQuestion}
	
	return render(request, 'katakanawords_manager/game.html', response)

@ensure_csrf_cookie
def checkanswer(request):
	global refreshable
	global currentQuestion
	global result
	if refreshable == False:
		guess = request.POST.get('input')
		if guess.lower() == correct_answer.lower():
			global score
			score+=1
			result = "Correct"
		else:
			result = "Incorrect. \nCorrect answer: " + correct_answer
		if currentQuestion >= 5:
			finalScore = 0.0 if score == 0 else ((score/5) * 100)
			result+="\n\nTotal score: " + str(finalScore) + "%"
		
		refreshable = True
	response = {'response' : question, 'result' : result, 'currentQuestion' : currentQuestion}
	return render(request, 'katakanawords_manager/game.html', response)
