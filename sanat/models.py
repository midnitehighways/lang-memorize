from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
	fi = models.TextField(max_length=50)
	en = models.TextField(max_length=100)
	TYPES = (
				('V', 'Verb'),#'Verbi'), 
				('S', 'Substantive'),#'Substantiivi'),
				('A', 'Adjective'),#'Adjektiivi'),
				('D', 'Adverb'),#'Adverbi'),
				('M', 'Other'),#'Jotain muuta'),
				('E', 'Not mentioned'),#'Ei mitaan'),
			)
	word_type = models.TextField(choices = TYPES, default='E')
	#userid = models.SmallIntegerField(default=0)
	#useruid = models.TextField(default='0')
	user = models.ForeignKey(User, null=True)
	show_in_common = models.BooleanField(default=True)
	
	def word_type_verbose(self):
		return dict(Word.TYPES)[self.word_type]
	
	def __str__(self):
		return '%s - %s' % (self.fi, self.en)


class Example(models.Model):		
	word = models.ForeignKey(Word)
	fi = models.TextField(max_length=100, default='')
	en = models.TextField(max_length=100, default='')
	
	def __str__(self):
		return '%s: %s' % (self.word.fi, self.fi)

# class UserProfile(models.Model):
#  	user = models.OneToOneField(User)
#  	show_in_common = models.BooleanField(default=True)
