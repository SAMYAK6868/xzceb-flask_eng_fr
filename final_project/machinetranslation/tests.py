import unittest
from translator import englishtofrench, frenchtoenglish

class Testfrenchtoenglish(unittest.TestCase):
    def test1(self):
        ##self.assertEqual(frenchtoenglish(""),"")
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")

class Testenglishtofrench(unittest.TestCase):
    def test1(self):
        ##self.assertEqual(englishtofrench(""),"")
        self.assertEqual(englishtofrench("Hello"),"Bonjour")

unittest.main()