#Class Member will construct a "member" to be added to our dictionary, each member must have some basic information over themselves
import unittest
import operator


memberList = {}#This is our list in the form of a dictionary


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


def addToList(allCardNumber, lastName, firstName, gradYear, position, email, major, minor):
	member = Member(allCardNumber, lastName, firstName, gradYear, position, email, major, minor)
	memberList[allCardNumber] = member

def removeFromList(allCardNumber):
	del memberList[allCardNumber]

#Looking up information of a club member will be done with the All Card Number

def getLastName(allCardNUmber):

def getFirstName(allCardNumber):

def getGradYear(allCardNumber):

def getEmail(allCardNumber):

def getMajor(allCardNumber):

def getMinor(allCardNumber):
        

def printList():
	print memberList	
