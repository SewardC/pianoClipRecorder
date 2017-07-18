from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Clips(models.Model):
	user = models.ForeignKey(User)
	clip_name = models.CharField(max_length = 50)
	key_flow = models.CharField(max_length = 250)
	key_respective_space = models.CharField(max_length = 250)
	key_used = models.CharField(max_length = 30)
	key_frequency = models.CharField(max_length = 30)
	is_favorite = models.BooleanField(default = False)

	def __str__(self):
		return self.clip_name