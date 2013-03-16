from django.db import models

# Create your models here.
class Event(models.Model):
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	description=models.TextField()
	start=models.DateTimeField('Start Date')
	end=models.DateTimeField('End Date')
	def __unicode__(self):
		return self.name
