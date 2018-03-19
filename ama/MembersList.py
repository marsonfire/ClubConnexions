#Class will import member class and this Members list will have getters and setters for
#the whole list of members
import unittest
import operator

class Member(object):
	allCardNumber = 0
	lastName = ""
	firstName = ""
	gradYear = ""
	position = ""
	email = ""
	major = ""
	minor = ""
	def __init__(self, allCardNumber, lastName, firstName, gradYear, position, email, major, minor):
		self.allCardNumber = allCardNumber
		self.lastName = lastName
		self.firstName = firstName
		self.gradYear = gradYear
		self.position = position
		self.email = email
		self.major = major
		self.minor = minor
	

memberList = {}#This is our list in the form of a dictionary




#To add/remove to the list we will have the all card number as the key and MemberClass(obj) is the value

def addToList(self, allCardNumber, lastName, firstName, gradYear, position, email, major, minor):
	member = Member(allCardNumber, lastName, firstName, gradYear, position, email, major, minor)
	memberList[allCardNumber] = member

def removeFromList(self, allCardNumber):
	del memberList[allCardNumber]

def printList(self):
	print memberList	
