#Author EJ Cervantes
#March 2018
#Member class describes what a member is made of and what inputs we require to make a member. 
#memberList is our dictionary. We use their all card as the key (because everyone has a unique all card number. We will have an object Member as our value. Retrieving information from a student will require their all card number
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
#Looking up information of a club member will be done with the All Card Number


def addToList(allCardNumber, lastName, firstName, gradYear, position, email, major, minor):
        member = Member(allCardNumber, lastName, firstName, gradYear, position, email, major, minor)
        memberList[allCardNumber] = member

def removeFromList(allCardNumber):
        del memberList[allCardNumber]

def getLastName(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "Last Name is: "
        print memberLookUp.lastName

def getFirstName(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "First Name is: "
        print memberLookUp.firstName

def getGradYear(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "Graduation year is: "
        print memberLookUp.gradYear

def getEmail(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "Email is: "
        print memberLookUp.email

def getMajor(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "Major is: "
        print memberLookUp.major

def getMinor(allCardNumber):
        memberLookUp = memberList[allCardNumber]
        print "Minor is: "
        print memberLookUp.minor

def printList():
        print memberList        


#Unit test that adds one person into dictionary.
#Expecting to print information about the member first
#Then expecting print of the dictionary in form of [key:value] where value is a spot in memory
#Then remove that member from dictionary, prints empty dictionary        
class MemberTesting(unittest.TestCase):
        
        def testAddRemoveMember(self):
                addToList(1234, "Cervantes", "Edwin", 2020, "Member", "cervantese@xavier.edu", "cs", "math")
                getLastName(1234)
                getFirstName(1234)
                getGradYear(1234)
                getEmail(1234)
                getMajor(1234)
                getMinor(1234)
                printList()
                removeFromList(1234)
                printList()

if __name__ == '__main__':
        unittest.main()
