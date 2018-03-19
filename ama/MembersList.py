#Class will import member class and this Members list will have getters and setters for
#the whole list of members
import unittest
import operator
from MemberClass import Member

memberList = {}#This is our list in the form of a dictionary




#To add/remove to the list we will have the all card number as the key and MemberClass(obj) is the value

def addToList(self, allCardNumber, MemberClass):
	memberList[allCardNumber] = MemberClass

def removeFromList(self, allCardNumber):
	del memberList[allCardNumber]

def printList(self):
	print memberList
