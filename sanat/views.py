# -*- coding: utf-8 -*-
from sanat import models
from django.shortcuts import render, get_object_or_404, render_to_response, redirect  ###
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse # needed for WordFrom
from .forms import WordForm, ExampleForm
import json
from django.core import serializers
from django.contrib.auth import logout as auth_logout 	###
from django.contrib.auth.decorators import login_required  ###
from django.contrib import messages

# -*- coding: utf-8 -*-
def index(request):
	if request.user.is_authenticated():
		words_list = models.Word.objects.order_by('-fi').filter(user=request.user)
	else:
		words_list = models.Word.objects.order_by('-fi').filter(show_in_common=True)
	context = {
		'words_list': words_list,
		'site_title': "Home | Puhun suomea",
		'is_common': False,									# which particular vocabulary user wants to display - common or own?
		}
	return render(request, "sanat/index.html", context,)

@login_required
def common(request):										# uses the same template as index.view, displays common vocabulary for logged-in user
	words_list = models.Word.objects.order_by('-fi').filter(show_in_common=True)#.exclude(user=request.user) 
	context = {
		'words_list': words_list,
		'site_title': "Common vocabulary | Puhun suomea",
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
		'site_title':"Test | Puhun suomea"
		}
	return render(request, "sanat/take_a_test.html", context,)

def settings(request):
	context = {
		'site_title':"Settings | Puhun suomea",
		}
	if request.method == 'POST':
		test = request.POST.get('test','')
		test_scope = request.POST.get('test_scope','')
		request.session['test'] = test
		request.session['test_scope'] = test_scope
		if request.POST.get('show','') == "False": # need this, cause otherwise bool values would be in quotes: "True"/"False" instead of True/False
			show = False
		else:
			show = True
		request.session['show'] = show
		if request.user.is_authenticated():
			models.Word.objects.filter(user=request.user).update(show_in_common=show)		# set current user's words field 'show_in_common'
		messages.add_message(request, messages.SUCCESS, ' Settings successfully saved!')		# sending the success message
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
			word.tyyppi = form.cleaned_data['tyyppi']
			if request.user.is_authenticated():				# possibility to add words anonymously
				word.user = request.user
			word.save()
			messages.add_message(request, messages.SUCCESS, 'Hooray! Your word is added.')		# sending the success message
			return HttpResponseRedirect(reverse('insert_form'),)				# get back to the insert_form page
		#else:
	form = WordForm()
	return render(request, "sanat/insert_form.html",{'form':form,})

def add_example_form(request, id):
	if request.method == 'POST':
		word = get_object_or_404(models.Word, pk=id)
		form = ExampleForm(request.POST)
		if form.is_valid():
			example = form.save(commit=False)
			example.word = word
			example.fi = form.cleaned_data['fi']
			#example.en = form.cleaned_data['en']
			example.save()
			return HttpResponseRedirect('/')
	form = ExampleForm()
	return render(request, "sanat/index.html",{'form':form})

def delete_word(request, id):
    word = get_object_or_404(models.Word, pk=id).delete()
    return HttpResponseRedirect(reverse('index'))

def about(request):
	# collection = dir(request.user.social_auth)
	# collection = request.user.social_auth.get().id
	# collection = request.user.social_auth.values
	# collection = request.user.social_auth.get().uid
	context = {
		'words_list': models.Word.objects.order_by('-fi'),
		'site_title':"About | Puhun suomea",
		# 'users':collection,
		}
	return render(request, "sanat/about.html", context,)


def login(request):
    return render(request, 'sanat/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')