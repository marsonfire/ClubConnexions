from django.test import TestCase

from .models import Event
from .models import Officers
from .models import Members
from .models import Home

# Create your tests here.

class EventModelTest(TestCase):

	def test_getName(self):
		event = Event(eventName="TEST Event")
		self.assertEqual(event.eventName, event.getName())

	def test_getDate(self):
		event = Event(eventDate="TEST Date")
		self.assertEqual(event.eventDate, event.getDate())

	def test_getTime(self):
		event = Event(eventTime="TEST Time")
		self.assertEqual(event.eventTime, event.getTime())

	def test_getLocation(self):
		event = Event(eventLocation="TEST location")
		self.assertEqual(event.eventLocation, event.getLocation())

	def test_getDescription(self):
		event = Event(eventDescription="TEST description")
		self.assertEqual(event.eventDescription, event.getDescription())

class OfficersModelTest(TestCase):

	def test_getFirstName(self):
		o = Officers(officerFirstName="firstname")
		self.assertEqual(o.officerFirstName, o.getFirstName())

	def test_getLastName(self):
		o = Officers(officerLastName="lastname")
		self.assertEqual(o.officerLastName, o.getLastName())

	def test_getPosition(self):
		o = Officers(officerPosition="position")
		self.assertEqual(o.officerPosition, o.getPosition())


class MembersModelTest(TestCase):

	def test_getFirstName(self):
		m = Members(memberFirstName="firstname")
		self.assertEqual(m.memberFirstName, m.getFirstName())

	def test_getLastName(self):
		m = Members(memberLastName="lastname")
		self.assertEqual(m.memberLastName, m.getLastName())


class HomeModelTest(TestCase):

	def test_getNumber(self):
		h = Home(number="1")
		self.assertEqual(h.number, h.getNumber())

	def test_getDescription(self):
		h = Home(description="TEST description")
		self.assertEqual(h.description, h.getDescription())
