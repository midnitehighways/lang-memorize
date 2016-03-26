from django import template
from sanat import models

register = template.Library()

@register.simple_tag
def get_words_number(request):
	#words_number = -1		# assign some random value at first 
	if request.user.is_authenticated():
		words_list = models.Word.objects.order_by('-fi').filter(user=request.user)
		words_number = words_list.count()	 
	return words_number