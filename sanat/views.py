from sanat import models
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {
		'words_list': models.Word.objects.order_by('-fi'),
		'site_title':"Home | Puhun suomea"
		}
	return render(request, "sanat/index.html", context,)
