import os
import sys

class simple_class:
    people = None
    place = None
    def __init__(self, place, people):
        self.place = place
        self.people = people
    def change_data(self, place, people):
        self.place = place
        self.people = people
    def __dele(self):
        self.place = None
        self.people = None
    def remove(self):
        self.__dele()
    def get_data(self):
        my_list = [self.place, self.people]
        return my_list
