"We will make two classes. The first will be an object of Member which gets "
"and sets a single member. We will then have a second class of memberList"
"which contains a dictionary of all the members and has the methods"

class Member(object):
	def __init__(self, allCardNumber, lastName, firstName, gradYear, position, email, major, minor):
		self.allCardNumber = allCardNumber
		self.lastName = lastName
		self.firstName = firstName
		self.gradYear = gradYear
		self.position = position
		self.email = email
		self.major = major
		self.minor = minor
	
class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

def make_student(name, age, major):
    student = Student(name, age, major)
    return student
		
		
		
