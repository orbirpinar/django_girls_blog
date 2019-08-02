from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# title
# text
# author
# created_date
# published_date

class Post(models.Model):
	title = models.CharField(max_length=100,verbose_name='Başlık')
	text = models.TextField(verbose_name='Yazı')
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title
