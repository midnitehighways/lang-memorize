from django.db import models
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#  	user = models.OneToOneField(User)
#  	show_in_common = models.BooleanField(default=True)

class Word(models.Model):
	fi = models.TextField(max_length=50)
	en = models.TextField(max_length=100)
	TYYPIT = (
				('V', 'Verbi'), 
				('S', 'Substantiivi'),
				('A', 'Adjektiivi'),
				('D', 'Adverbi'),
				('M', 'Jotain muuta'),
				('E', 'Ei mitaan'),
			)
	tyyppi = models.TextField(choices = TYYPIT, default='E')
	#userid = models.SmallIntegerField(default=0)
	#useruid = models.TextField(default='0')
	user = models.ForeignKey(User, null=True)
	show_in_common = models.BooleanField(default=True)
	def __str__(self):
		return self.fi 

class Example(models.Model):		
	word = models.ForeignKey(Word)
	fi = models.TextField(max_length=100, default='')
	en = models.TextField(max_length=100, default='')
	def __str__(self):
		return self.word.fi
