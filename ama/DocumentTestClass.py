# Class: Document Test
# Author: Kara Schatz
# Last Edit: 4/03/2018

import unittest
from DocumentClass import Document

class ConstructorTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Officer Application'
        self.url = 'www.officerapplication.com'
        self.d = Document(self.name, self.url)

    def testName(self):
        name = self.d.getName()
        self.assertEqual(self.name, name)
    def testUrl(self):
        url = self.d.getUrl()
        self.assertEqual(self.url, url)

class SettersTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Event Flyer'
        self.url = 'www.eventflyer.com'
        self.d = Document()

    def testName(self):
        self.d.setName(self.name)
        self.assertEqual(self.name, self.d.getName())
    def testUrl(self):
        self.d.setUrl(self.url)
        self.assertEqual(self.url, self.d.getUrl())

class PrintTests(unittest.TestCase):
    def setUp(self):
        self.name = 'another essential document'
        self.url = 'www.anotheressentialdocument.com'
        self.d = Document(self.name, self.url)

    def testPrint(self):
        expected = print('name: another essential document',"\n", 'URL: www.anotheressentialdocument.com')
        actual = self.d.printDoc()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()        
