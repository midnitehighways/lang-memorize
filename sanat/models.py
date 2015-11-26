from django.db import models

class Word(models.Model):
	fi = models.TextField(max_length=50)
	en = models.TextField(max_length=100)
	TYYPIT = (
				('V', 'Verbi'), 
				('S', 'Substantiivi'),
				('E', 'Ei mitaan'),
			)
	tyyppi = models.TextField(choices = TYYPIT, default='E')
	
	def __str__(self):
		return self.fi 

class Example(models.Model):		
	word = models.ForeignKey(Word)
	fi = models.TextField(max_length=100, default='')
	en = models.TextField(max_length=100, default='')

	def __str__(self):
		return self.word.fi