from django.db import models
from django.utils import timezone

class Author(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length = 100)	
	author = models.ForeignKey(Author)
	price =  models.DecimalField(max_digits=12, decimal_places=4, default = 0)
	publish = models.DateField(default=timezone.now)
	def __str__(self):
		return self.title