from behave import *
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__).split('anagram')[0],"anagram"))
import unittest
from check_anagram import AnagramChecker
class TestCheckAnagram(unittest.TestCase):
    AnagramCheckerObj = AnagramChecker()
    def test_checkIsAnagramForAnagramStrings(self):
        self.assertEqual("is",self.AnagramCheckerObj.CheckIsAnagram("god", "dog"))

    def test_checkIsAnagramForNotAnagramStrings(self):
        self.assertEqual("is not",self.AnagramCheckerObj.CheckIsAnagram("god", "cut"))
    
    def test_checkIsAnagramForCaseAnagramStrings(self):
        self.assertEqual("is",self.AnagramCheckerObj.CheckIsAnagram("God", "Dog"))
    
    def test_checkIsAnagramForSpaceAnagramStrings(self):
        self.assertEqual("is",self.AnagramCheckerObj.CheckIsAnagram("G od ", "Do g"))

    def test_checkIsAnagramForOneAnagramStrings(self):
        self.assertEqual("is not",self.AnagramCheckerObj.CheckIsAnagram(" ", "Do g"))

    def test_checkIsAnagramForSpecialAnagramStrings(self):
        self.assertEqual("is not",self.AnagramCheckerObj.CheckIsAnagram("$god", "Dog$"))

    def test_checkIsAnagramForAlphanumericAnagramStrings(self):
        self.assertEqual("is not",self.AnagramCheckerObj.CheckIsAnagram("1god", "Dog1"))
    
    def test_checkIsAnagramForStrLenAnagramStrings(self):
        self.assertEqual("is not",self.AnagramCheckerObj.CheckIsAnagram("god", "godd"))


