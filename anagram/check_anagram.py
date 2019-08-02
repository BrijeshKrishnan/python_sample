
import re

class AnagramChecker():
    IS = "is"
    IS_NOT = "is not"
    def CheckIsAnagram(self, string_1, string_2):
        if not self.__is_valid_string(string_1) or not self.__is_valid_string(string_2):
            return self.IS_NOT
        subject = self.__pre_process_string(string_1)
        candidate = self.__pre_process_string(string_2)
        if self.__is_length_diff(subject, candidate):
            return self.IS_NOT
        return self.IS if self.__sort_string(subject) == self.__sort_string(candidate) else self.IS_NOT

    def __is_valid_string(self, string):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]') 
        return True if regex.search(string) == None else False

    def __is_length_diff(self, string_1, string_2):
        False if len(string_1) != len(string_2) else True

    def __pre_process_string(self, string):
        return str(string).strip().upper()

    def __sort_string(self, string):
        return ''.join(sorted(string))

