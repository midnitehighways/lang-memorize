from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-words$', views.insert_form, name='insert_form'),
	url(r'^(?P<id>[0-9]+)/add-example$', views.add_example_form, name='add_example_form'),
	url(r'^(?P<id>[0-9]+)/delete-word$', views.delete_word, name='delete_word'),
	url(r'^take-a-test$', views.take_a_test, name='take_a_test'),
	url(r'^about$', views.about, name='about'),
	#url(r'^add-to-DB$', views.add_to_DB, name='add_to_DB'),
]