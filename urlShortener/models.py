from django.db import models
from django.conf import settings
import random, string

def generate_key():
	return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8))

class Url(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)	
	linkTo = models.URLField()
	key = models.CharField(unique=True, max_length=20, default=generate_key)
	dateCreated = models.DateTimeField(auto_now_add=True)
	clicks = models.PositiveIntegerField(default=0)
	expires_at = models.DateTimeField(null=True, blank=True)

	@property
	def is_expired(self):
		from django.utils import timezone
		if self.expires_at and self.expires_at < timezone.now():
			return True
		return False

	def __str__(self):
		return f"{self.key} -> {self.linkTo}"

class LinkClick(models.Model):
	url = models.ForeignKey(Url, on_delete=models.CASCADE, related_name='click_details')
	timestamp = models.DateTimeField(auto_now_add=True)
	referrer = models.TextField(null=True, blank=True)
	user_agent = models.TextField(null=True, blank=True)
	ip_address = models.GenericIPAddressField(null=True, blank=True)