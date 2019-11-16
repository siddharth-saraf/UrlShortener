from django.db import models
from django.conf import settings
import random, string

class Url(models.Model):
	def generateKey():
		return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8))

	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)	
	linkTo = models.URLField()
	key = models.CharField(unique=True, max_length=20, default=generateKey)
	dateCreated = models.DateTimeField(auto_now_add=True)