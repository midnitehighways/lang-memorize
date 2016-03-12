from sanat import models
from django.shortcuts import render, get_object_or_404, render_to_response, redirect  ###
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse # needed for WordFrom
from .forms import WordForm, ExampleForm
import json
from django.core import serializers
from django.contrib.auth import logout as auth_logout 	###
from django.contrib.auth.decorators import login_required  ###

def index(request):
	context = {
		'words_list': models.Word.objects.order_by('-fi'),
		#'examples_list': models.Example.objects.order_by('-fi'),
		'site_title':"Home | Puhun suomea"
		}
	return render(request, "sanat/index.html", context,)

def insert_form(request):
	if request.method == 'POST':
		# userr = request.user
		# social = userr.social_auth.get(provider='twitter')
		# userid = request.user.social_auth.get().id
		form = WordForm(request.POST)
		if form.is_valid():
			word = form.save(commit=False)
			word.fi = form.cleaned_data['fi']
			word.en = form.cleaned_data['en']
			word.tyyppi = form.cleaned_data['tyyppi']
			# word.user = userr
			word.user = request.user
			# word.userid = request.user.social_auth.get().id
			# word.useruid = request.user.social_auth.get().uid
			word.save()
			return HttpResponseRedirect('/')
		#else:
	form = WordForm()
	return render(request, "sanat/insert_form.html",{'form':form})

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
# @login_required(login_url='/take_a_test')
def take_a_test(request):
	data = serializers.serialize("json", models.Word.objects.all())
	context = {
		'words_list': data,
		'site_title':"Test | Puhun suomea"
		}
	return render(request, "sanat/take_a_test.html", context,)

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