from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	major=models.CharField(max_length=100)
	user=models.ForeignKey(User, unique=True)
	gradmonth=models.CharField(max_length=20)
	gradyear=models.CharField(max_length=20)
	email_subscribed=models.BooleanField()
	activated=models.BooleanField()
	interests=models.TextField()
	@property
	def firstName(self):
		return self.user.first_name
	@property
	def lastName(self):
		return self.user.last_name
	@property
	def email(self):
		return self.user.email
