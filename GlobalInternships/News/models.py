from django.db import models

# Create your models here.
class NewsItem(models.Model):
	title=models.CharField(max_length=100)
	imageURL=models.CharField(max_length=200)
	author=models.CharField(max_length=100)
	pub_date=models.DateTimeField('Date Published')
	article=models.TextField()

	def __unicode__(self):
		return self.title
