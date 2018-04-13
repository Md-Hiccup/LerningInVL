from django.http import HttpResponse		
from django.shortcuts import render, get_object_or_404
# from django.template import loader		3

from .models import Question 				
# Create your views here.

def index(request):
	# 4
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = { 'latest_question_list' : latest_question_list }
	return render(request, 'polls/index.html', context)

	# 3
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = {
	# 	'latest_question_list': latest_question_list,
	# }
	# return HttpResponse(template.render(context, request))
	
	# 2
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# ouput = ",  ".join([q.question_text for q in latest_question_list])
	# return HttpResponse(ouput)

	# 1
	# return HttpResponse("Hello World. You are at the polls index.")


def polls(request):
	return HttpResponse("Hello from polls function");

def detail(request, question_id):
	# 3
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', { 'question': question })

	#  2
	# try:
	# 	question = Question.objects.get(pk = question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	# return render(request, 'polls/detail.html', { 'question': question})

	#  1
	# return HttpResponse("You are looking for question %s. " % question_id)		1
	
def results(request, question_id):
	response = "You're looking at the result of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s. " % question_id)