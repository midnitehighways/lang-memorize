from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-words$', views.insert_form, name='insert_form'),
	#url(r'^add-to-DB$', views.add_to_DB, name='add_to_DB'),
]