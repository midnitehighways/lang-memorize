from sanat import models
from django.shortcuts import render, get_object_or_404, render_to_response, redirect  ###
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse # needed for WordForm
from .forms import WordForm, ExampleForm
import json
from django.core import serializers
from django.contrib.auth import logout as auth_logout 	###
from django.contrib.auth.decorators import login_required  ###
from django.contrib import messages
# from django.views.decorators.csrf import ensure_csrf_cookie
# -*- coding: utf-8 -*-
def index(request):
	if 'test_scope' not in request.session:				# set default settings
		request.session['test_scope'] = 'common'		# if there's no key in session - add value (use common by default)
	if 'test' not in request.session:					
		request.session['test'] = 'classic'
	if 'show' not in request.session:					
		request.session['show'] = 'True'

	if request.user.is_authenticated():
		words_list = models.Word.objects.order_by('fi').filter(user=request.user)
	else:
		words_list = models.Word.objects.order_by('fi').filter(show_in_common=True)
	context = {
		'words_list': words_list,
		'site_title': "Home | WWWords",
		'is_common': False,									# which particular vocabulary user wants to display - common or own?
		}
	return render(request, "sanat/index.html", context,)

@login_required
def common(request):										# uses the same template as index.view, displays common vocabulary for logged-in user
	words_list = models.Word.objects.order_by('fi').filter(show_in_common=True)#.exclude(user=request.user) 
	context = {
		'words_list': words_list,
		'site_title': "Common vocabulary | WWWords",
		'is_common': True,
		}
	return render(request, "sanat/index.html", context,)

# @login_required(login_url='/take_a_test')
def take_a_test(request):
	if 'test_scope' not in request.session:					# if there's no key in session - add value (use common by default)
		request.session['test_scope'] = 'common'
	if request.user.is_authenticated() and request.session['test_scope'] == 'own':
		data = serializers.serialize("json", models.Word.objects.filter(user=request.user))		# pick only current user's words
	else:
		data = serializers.serialize("json", models.Word.objects.filter(show_in_common=True))
	context = {
		'words_list': data,
		'site_title':"Test | WWWords"
		}
	return render(request, "sanat/take_a_test.html", context,)

def settings(request):
	context = {
		'site_title':"Settings | WWWords",
		}
	if request.method == 'POST':
		test = request.POST.get('test','')
		request.session['test'] = test
		if request.user.is_authenticated():
			if request.POST.get('show','') == "False": # need this, otherwise bool values would be in quotes: "True"/"False" instead of True/False
				show = False
			else:
				show = True
			request.session['show'] = show
			models.Word.objects.filter(user=request.user).update(show_in_common=show)		# set current user's words field 'show_in_common'

			test_scope = request.POST.get('test_scope','')
			if models.Word.objects.filter(user=request.user).count() < 4 and test_scope == "own": # if user tries to save to "own" and has less than 4 words in own vocabulary
				messages.add_message(request, messages.WARNING, 
				'Not enough words in own vocabulary to take a test. Other settings saved.')		# sending the warning message
			else:
				messages.add_message(request, messages.SUCCESS, ' Settings successfully saved!')		# sending the success message
				request.session['test_scope'] = test_scope
		else:
			messages.add_message(request, messages.WARNING, 
			'You must be logged in to work with own vocabulary. Other settings saved for anonymous session.')		# sending the warning message
		#messages.add_message(request, messages.SUCCESS, ' Settings successfully saved!')		# sending the success message
		return HttpResponseRedirect(reverse('settings'),)
	return render(request, "sanat/settings.html", context,)

def insert_form(request):
	if request.method == 'POST':
		# userid = request.user.social_auth.get().id
		form = WordForm(request.POST)
		if form.is_valid():
			word = form.save(commit=False)
			word.fi = form.cleaned_data['fi']
			word.en = form.cleaned_data['en']
			word.word_type = form.cleaned_data['word_type']
			if request.user.is_authenticated():				# possibility to add words anonymously
				word.user = request.user					# set current user as word's "owner"
			word.save()
			messages.add_message(request, messages.SUCCESS, 'Hooray! Your word is added.')		# sending the success message
			return HttpResponseRedirect(reverse('insert_form'),)				# get back to the insert_form page
		#else:
	form = WordForm()
	return render(request, "sanat/insert_form.html",{'form':form,})

# @ensure_csrf_cookie
def add_example_form(request, id):
	if request.method == 'POST':
		word = get_object_or_404(models.Word, pk=id)
		example_text = request.POST.get('example_text')
		example = models.Example(word=word, fi=example_text)
		# example.fi = request.POST.get('example_text')
		example.save()
		number = models.Example.objects.filter(word=word).count()	# get the number of examples to a given word
		response_data = {}
		# response_data['result'] = 'Example added successfully!'
		response_data['number'] = number
		response_data['example'] = example_text
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	form = ExampleForm()
	return render(request, "sanat/index.html",{'form':form})

def edit_word(request, id):
	if request.method == 'POST':
		word = get_object_or_404(models.Word, pk=id)
		word.fi = request.POST.get('fi_word')
		word.en = request.POST.get('en_word')
		word.save()
	return HttpResponse()

def delete_word(request, id):
    word = get_object_or_404(models.Word, pk=id)
    if request.user.is_authenticated() and word.user == request.user:
    	word.delete()
    	messages.add_message(request, messages.SUCCESS, "Word deleted successfully")		# sending the success message
    else:
    	messages.add_message(request, messages.WARNING, "Can delete own words only")		# sending the success message
    # return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(request.GET.get('next', '/'))

def about(request):
	# collection = dir(request.user.social_auth)
	# collection = request.user.social_auth.get().id
	# collection = request.user.social_auth.values
	# collection = request.user.social_auth.get().uid
	# context = {
	# 	'words_list': models.Word.objects.order_by('fi'),
	# 	'site_title':"About | Puhun suomea",
	# 	# 'users':collection,
	# 	}
	context = {
		'site_title':"About | WWWords",
		}
	return render(request, "sanat/about.html", context,)

def start(request):
	context = {
		'site_title':"Welcome | WWWords",
		}
	return render(request, "sanat/start.html", context,)

def login(request):
    return render(request, 'sanat/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/')) # redirect to current page after logout (specified in template: ?next={{request.path}})