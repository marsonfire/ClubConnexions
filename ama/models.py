from django.db import models

# Create your models here.
class Description(models.Model):
	descText = models.CharField(max_length = 400)

	def str(self):
		return self.descriptionText
	
