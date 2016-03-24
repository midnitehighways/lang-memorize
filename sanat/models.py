from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
	fi = models.TextField(max_length=50)
	en = models.TextField(max_length=100)
	TYYPIT = (
				('V', 'Verb'),#'Verbi'), 
				('S', 'Substantive'),#'Substantiivi'),
				('A', 'Adjective'),#'Adjektiivi'),
				('D', 'Adverb'),#'Adverbi'),
				('M', 'Else'),#'Jotain muuta'),
				('E', 'Not mentioned'),#'Ei mitaan'),
			)
	tyyppi = models.TextField(choices = TYYPIT, default='E')
	#userid = models.SmallIntegerField(default=0)
	#useruid = models.TextField(default='0')
	user = models.ForeignKey(User, null=True)
	show_in_common = models.BooleanField(default=True)
	
	def tyyppi_verbose(self):
		return dict(Word.TYYPIT)[self.tyyppi]
	def __str__(self):
		return self.fi 

class Example(models.Model):		
	word = models.ForeignKey(Word)
	fi = models.TextField(max_length=100, default='')
	en = models.TextField(max_length=100, default='')
	def __str__(self):
		return self.word.fi

# class UserProfile(models.Model):
#  	user = models.OneToOneField(User)
#  	show_in_common = models.BooleanField(default=True)
