from django.db import models

# Create your models here.

class Event(models.Model):
	eventName = models.CharField(max_length=200)
	eventDate = models.CharField(max_length=50)
	eventTime = models.CharField(max_length=50)
	eventLocation = models.CharField(max_length=200)
	eventDescription = models.CharField(max_length=1000)

	class Meta:
		ordering = ['eventDate', 'eventTime']

	def getName(self):
		name = self.eventName
		return name
		
	def getDate(self):
		return self.eventDate

	def getTime(self):
		return self.eventTime

	def getLocation(self):
		return self.eventLocation

	def getDescription(self):
		return self.eventDescription

class Officers(models.Model):
	officerFirstName = models.CharField(max_length=50)
	officerLastName = models.CharField(max_length=50)
	officerPosition = models.CharField(max_length=50)

	class Meta:
		ordering = ['officerLastName', 'officerFirstName']

	def getFirstName(self):
		return self.officerFirstName

	def getLastName(self):
		return self.officerLastName

	def getPosition(self):
		return self.officerPosition

class Members(models.Model):
	memberFirstName = models.CharField(max_length=50)
	memberLastName = models.CharField(max_length=50)
	memberEmail = models.CharField(max_length=50)
	memberID = models.CharField(max_length=10)

	class Meta:
		ordering = ['memberLastName', 'memberFirstName']

	def getFirstName(self):
		return self.memberFirstName

	def getLastName(self):
		return self.memberLastName

	def getEmail(self):
		return self.memberEmail

	def getID(self):
		return self.memberID
		
class Home(models.Model):
	number = models.CharField(max_length=1)
	description = models.CharField(max_length=1000)

	def getNumber(self):
		return self.number

	def getDescription(self):
		return self.description


