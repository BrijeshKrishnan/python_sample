from behave import given, when, then, step
import os
import sys
import unittest 
sys.path.append(os.path.join(os.path.dirname(__file__).split('anagram')[0],"anagram"))

from check_anagram import AnagramChecker

actualMessage = None
def ConnectAnagramChecker(subject, candidate):
    AnagramCheckerObj = AnagramChecker()
    return AnagramCheckerObj.CheckIsAnagram(subject, candidate)

@when(u'I ask if the word or phrase {subject} is an anagram of the word or phrase {candidate}')
def test_anagram_failure(context, subject, candidate):
    context.actualMessage = ConnectAnagramChecker(subject, candidate)

@then("I see a message - can not check for anagram because {expectedExceptionMessage}")
def validateException(context, expectedExceptionMessage):
    if '"' in  expectedExceptionMessage:
        expectedExceptionMessage = expectedExceptionMessage.strip('"')
    print('********This is a log message %s'%expectedExceptionMessage)
    assert(expectedExceptionMessage ==  context.actualMessage)

@then(u'I see a message {candidate} {result} an anagram of {subject}')
def validatepass(context, candidate, result, subject):
    if '"' in  result:
        result = result.strip('"')
    assert(result ==  context.actualMessage)