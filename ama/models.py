from django.db import models

# Create your models here.

class Event(models.Model):
	eventName = models.CharField(max_length=200)
	eventDate = models.CharField(max_length=50)
	eventTime = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=200)
	eventDescription = models.CharField(max_length=1000)

	@classmethod
	def create(cls, eventName, eventDate, eventTime, eventLocation, eventDescription):
		e = cls(eventName, eventDate, eventTime, eventLocation, eventDescription)
		return e

	def _str_(self):
		return self.eventName

	def _str_(self):
		return self.eventDate

	def _str_(self):
		return self.eventTime

	def _str_(self):
		return self.eventLocation

	def _str_(self):
		return self.eventDescription

class Officers(models.Model):
	officerFirstName = models.CharField(max_length=50)
	officerLastName = models.CharField(max_length=50)
	officerPosition = models.CharField(max_length=50)

	@classmethod
	def create(cls, officerFirstName, officerLastName, officerPosition):
		o = cls(officerFirstName, officerLastName, officerPosition)
		return o

	def _str_(self):
		return self.officerFirstName

	def _str_(self):
		return self.officerLastName

	def _str_(self):
		return self.officerPosition

class Members(models.Model):
	memberFirstName = models.CharField(max_length=50)
	memberLastName = models.CharField(max_length=50)
	officerPosition = models.CharField(max_length=50)

	@classmethod
	def create(cls, officerFirstName, officerLastName, officerPosition):
		o = cls(officerFirstName, officerLastName, officerPosition)
		return o

	def _str_(self):
		return self.memberFirstName

	def _str_(self):
		return self.memberLastName




