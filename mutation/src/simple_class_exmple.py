import os
import sys
sys.path.append(os.path.join((os.path.dirname(__file__))))
from util import return_data
class simple_class:
    patient = None
    patient_id = None
    def __init__(self, patient, patient_id):
        self.patient = patient
        self.patient_id = patient_id
    def change_data(self, patient, patient_id):
        self.patient = patient
        self.patient_id = patient_id
    def __dele(self):
        self.patient = None
        self.patient_id = None
    def remove(self):
        self.__dele()
    def get_data(self):
        my_list = [self.patient, self.patient_id]
        print (return_data())
        return my_list
    def value_mutation(self):
        if self.patient_id > 100:
            return "New Patient"
        else:
            return "Existing Patient"

