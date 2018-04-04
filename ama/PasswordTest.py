import unittest
from Password import Password

class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.testPassword = ' '
        self.p = Password(' ')
    def testCreatePassword(self):
        self.testPassword= self.p.createPassword('ScottIsBest')
        expected = 'ScottIsBest'
        self.assertEqual(expected,self.testPassword)
        
class PasswordTest1(unittest.TestCase):
    def setUp(self):
        self.testPassword = ' '
        self.p = Password(' ')
    def testCreatePassword(self):
        self.testPassword= self.p.createPassword('ScottIsNotBest')
        expected = 'ScottIsBest'
        self.assertNotEqual(expected,self.testPassword)
        
class PasswordTest2(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin =True

    def testEditPassword(self):
        self.testEditPassword= self.p.editPassword('pass','new','new')
        expected= 'new'
        self.assertEqual(expected, self.testEditPassword)

class PasswordTest3(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin =True

    def testEditAdmin(self):
        self.testEditPassword= self.p.editPassword('notPass','new','new')
        expected= 'new'
        self.assertNotEqual(expected, self.testEditPassword)
        
class PasswordTest4(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin =False

    def testEditAdmin(self):
        self.testEditPassword= self.p.editPassword('Pass','new','new')
        expected= 'new'
        self.assertNotEqual(expected, self.testEditPassword)
        
class PasswordTest5(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin = True

    def testEditAdmin(self):
        self.testEditPassword= self.p.editPassword('notPass','new','notNew')
        expected= 'new'
        self.assertNotEqual(expected, self.testEditPassword)
        
class PasswordTest6(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin = False
        
    def testEnableAdmin(self):
        self.test = False
        self.test= self.p.enableAdmin('pass')
        expected = True
        self.assertEqual(self.test, expected)
class PasswordTest7(unittest.TestCase):
    def setUp(self):
        self.p = Password('pass')
        self.p.boolAdmin = False
        
    def testEnableAdmin(self):
        self.test = False
        self.test= self.p.enableAdmin('notPass')
        expected = False
        self.assertEqual(self.test, expected)

if __name__ == '__main__':
    unittest.main()
