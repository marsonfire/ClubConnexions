# Class: Event Test
# Author: Kara Schatz
# Last Edit: 4/03/2018

import unittest
from EventClass import Event

class ConstructorTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Group Meeting'
        self.date = '03152018'
        self.time = '1830'
        self.location = 'Hailstones 19'
        self.description = 'meeting to work on project'
        self.e = Event(self.name, self.date, self.time, self.location, self.description)

    def testName(self):
        name = self.e.getName()
        self.assertEqual(self.name, name)
    def testDate(self):
        date = self.e.getDate()
        month = self.date[:2]
        day = self.date[2:4]
        year = self.date[4:]
        expected = month + '/' + day + '/' + year
        self.assertEqual(expected, date)
    def testTime(self):
        time = self.e.getTime()
        hour = self.time[:2]
        minute = self.time[2:]
        expected = hour + ':' + minute
        self.assertEqual(expected, time)
    def testLocation(self):
        location = self.e.getLocation()
        self.assertEqual(self.location, location)
    def testDescription(self):
        description = self.e.getDescription()
        self.assertEqual(self.description, description)

class SettersTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Software Engineering Class'
        self.date = '03132018'
        self.time = '1000'
        self.location = 'Alter 208'
        self.description = 'null'
        self.e = Event()

    def testName(self):
        self.e.setName(self.name)
        self.assertEqual(self.name, self.e.getName())
    def testDate(self):
        self.e.setDate(self.date)
        month = self.date[:2]
        day = self.date[2:4]
        year = self.date[4:]
        expected = month + '/' + day + '/' + year
        self.assertEqual(expected, self.e.getDate())
    def testTime(self):
        self.e.setTime(self.time)
        hour = self.time[:2]
        minute = self.time[2:]
        expected = hour + ':' + minute
        self.assertEqual(expected, self.e.getTime())
    def testLocation(self):
        self.e.setLocation(self.location)
        self.assertEqual(self.location, self.e.getLocation())
    def testDescription(self):
        self.e.setDescription(self.description)
        self.assertEqual(self.description, self.e.getDescription())

class PrintTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Basketball Game'
        self.date = '03162018'
        self.time = '1940'
        self.location = 'Bridgestone Arena'
        self.description = 'Xavier vs. Texas Southern in NCAA First Round'
        self.e = Event(self.name, self.date, self.time, self.location,
                       self.description)
##        self.e = Event('Basketball Game', '03162018', '1940', 'Bridgestone Arena',
##                       'Xavier vs. Texas Southern in NCAA First Round')

    def testPrint(self):
        #expected = ('name:', self.name, ', date:', self.date,
         #     ', time:', self.time, ', location:',
          #    self.location, ', description:', self.description)
        expected = print('name: Basketball Game , date: 03/16/2018 , '
                    'time: 19:40 , location: Bridgestone Arena , '
                    'description: Xavier vs. Texas Southern in '
                    'NCAA First Round')
        actual = self.e.printEvent()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()        
