from CalendarClass import Calendar
from EventClass import Event
import unittest

class CalendarTest(unittest.TestCase):
    def setUp(self):
        #e = Event('Group Meeting','031512018','1830',
         #         'Hailstones 19','meeting to work on project')
        self.listOfEvents = {} #{'Group Meeting': e}

    def testAdd(self):
        e = Event('Group Meeting','031512018','1830',
                  'Hailstones 19','meeting to work on project')
        
