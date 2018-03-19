from EventClass import Event
import unittest

class ConstructorTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Group Meeting'
        self.date = '03152018'
        self.time = '1830'
        self.location = 'Hailstones 19'
        self.description = 'meeting to work on project'
        e = Event(self.name, self.date, self.time, self.location, self.description)

    def testName(self):
        name = e.getName()
        self.assertEqual(self.name, name)
    def testDate(self):
        date = e.getDate()
        month = self.date[:2]
        day = self.date[2:4]
        year = self.date[4:]
        expected = month + '/' + day + '/' + year
        self.assertEqual(expected, date)
    def testTime(self):
        time = e.getTime()
        hour = self.time[:2]
        minute = self.time[2:]
        expected = hour + ':' + minute
        self.assertEqual(expected, time)
    def testLocation(self):
        location = e.getLocation()
        self.assertEqual(self.location, location)
    def testDescription(self):
        description = e.getDescription()
        self.assertEqual(self.description, description)

class SettersTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Software Engineering Class'
        self.date = '03132018'
        self.time = '1000'
        self.location = 'Alter 208'
        self.description = 'null'
        e = Event()

    def testName(self):
        e.setName(self.name)
        self.assertEqual(self.name, e.getName)
    def testDate(self):
        e.setDate(self.date)
        month = self.date[:2]
        day = self.date[2:4]
        year = self.date[4:]
        expected = month + '/' + day + '/' + year
        self.assertEqual(expected, e.getDate)
    def testTime(self):
        e.setTime(self.ime)
        hour = self.time[:2]
        minute = self.time[2:]
        expected = hour + ':' + minute
        self.assertEqual(expected, e.getTime)
    def testLocation(self):
        e.setLocation(self.location)
        self.assertEqual(self.location, e.getLocation)
    def testDescription(self):
        e.setDescription(self.description)
        self.assertEqual(self.description, e.getDescription)

class PrintTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Basketball Game'
        self.date = '03162018'
        self.time = '1940'
        self.location = 'Bridgestone Arena'
        self.description = 'Xavier vs. Texas Southern in NCAA First Round'
        e = Event(self.name, self.date, self.time, self.location)
        
    def testPrint(self):
        event = e.printEvent()
        expected = ('name:', self.name, ', date:', self.date,
              ', time:', self.time, ', location:',
              self.location, ', description:', self.description)
        #expected = ('name: Basketball Game, date: 03/16/2018, '
         #           'time: 19:40, location: Bridgestone Arena, '
          #          'description: Xavier vs. Texas Southern in '
           #         'NCAA First Round')
        self.assertEqual(expected, event)
