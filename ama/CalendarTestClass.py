from CalendarClass import Calendar
from EventClass import Event
import unittest

class CalendarTest(unittest.TestCase):
    def setUp(self):
        #e = Event('Group Meeting','031512018','1830',
         #         'Hailstones 19','meeting to work on project')
        self.c = Calendar()
        #self.listOfEvents = {} #{'Group Meeting': e}

    def testAdd(self):
        e = Event('Group Meeting','03152018','1830',
                  'Hailstones 19','meeting to work on project')
        self.c.addEvent(e)
        expected = {'Group Meeting': e}
        self.assertEqual(expected, self.c.listOfEvents)

    def testPrint(self):
        e = Event('Group Meeting','03152018','1830',
                  'Hailstones 19','meeting to work on project')
        f = Event('Software Engineering Class','03202018','1000',
                  'Alter 208')
        self.c.addEvent(e)
        self.c.addEvent(f)
        expected = '''Event #1 is:
            name: Group Meeting , date: 03/15/2018 , time: 18:30 , location: Hailstones 19 , description: meeting to work on project
            Event #2 is:
            name: Software Engineering Class , date: 03/20/2018 , time: 10:00 , location: Alter 208 , description: null
            '''
        expected = print(expected)
        result = self.c.printList()
        self.assertEqual(expected, result)
        
    def testDisplay(self):
        e = Event('Group Meeting','03152018','1830',
                  'Hailstones 19','meeting to work on project')
        self.c.addEvent(e)
        expected = ('The Event Group Meeting is on 03/15/2018 at 18:30 '
                    'in Hailstones 19. The following is a description of '
                    'the event: meeting to work on project')
        result = self.c.displayEvent(e)
        self.assertEqual(expected, result)

    def testDelete(self):
        e = Event('Software Engineering Class','03202018','1000',
                  'Alter 208')
        self.c.addEvent(e)
        expected = None
        result = self.c.printList()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
