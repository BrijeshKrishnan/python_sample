
import re

def singleton(cls): 
    """
    class to provide instance to make sure its a singleton
    """   
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper
    
@singleton    
class AnagramChecker():
    """
    singleton class to check if a given pair of strings are anagram of eachother
    """
    IS = "is"
    IS_NOT = "is not"
    MESSAGE = None
    def __init__(self):
        pass
    def CheckIsAnagram(self, string_1, string_2):   
        """
        function which check whether two strings are anagram of eachother or not
        """  
        if not self.__is_valid_string(string_1) or not self.__is_valid_string(string_2):
            self.MESSAGE="Subject or Candidate is not valid String"
            return self.MESSAGE
        subject = self.__pre_process_string(string_1)
        candidate = self.__pre_process_string(string_2)
        print(subject)
        print(candidate)
        if not self.__is_length_diff(subject, candidate):
            self.MESSAGE="Subject or Candidate length does not match"
            return self.MESSAGE
        self.MESSAGE = self.IS if self.__sort_string(subject) == self.__sort_string(candidate) else self.IS_NOT
        return self.MESSAGE

    def __is_valid_string(self, string):
        """
        function to check of the given string contains special characters or not
        """
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]') 
        return True if regex.search(string) == None else False

    def __is_length_diff(self, string_1, string_2):
        """
        function to check length of two given strings 
        """
        return False if len(string_1) != len(string_2) else True

    def __pre_process_string(self, string):
        """
        function to process the given string to remove the empty space, make the string to uppercase
        """
        return str(string).upper().replace(" ", "")

    def __sort_string(self, string):
        """
        Function that sort the character in a string
        """
        return ''.join(sorted(string))