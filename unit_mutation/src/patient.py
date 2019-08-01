import os
import sys
sys.path.append(os.path.join((os.path.dirname(__file__))))
from patient_utility import return_message
class PatientClass:
    """ 
    This is a class for creating the patient details with patient ID 
      
    Attributes: NA
    """
    patient = None
    patient_id = None
    def __init__(self, patient, patient_id):
        """ 
        The constructor for PatientClass class. 
  
        Parameters: 
           patient: name of the patient. 
           patient_id: patient ID.    
        """
        self.patient = patient
        self.patient_id = patient_id
    def change_data(self, patient, patient_id):
        """ 
        Function to change the data which was initialized by constructor
  
        Parameters: 
           patient: name of the patient. 
           patient_id: patient ID.    
        """
        self.patient = patient
        self.patient_id = patient_id
    def __dele(self):
        """ 
        Private function to delete the patient and patient_id created. 
  
        Parameters: NA  
        """
        self.patient = None
        self.patient_id = None
    def remove(self):
        """ 
        Function which is exposed outside to delete the patient and patient_id created. 
  
        Parameters: NA  
        """
        self.__dele()
    def get_data(self):
        """ 
        Function which is used to fetch the patient and patient_id created. 
  
        Parameters: NA  
        """
        my_list = [self.patient, self.patient_id]
        print (return_message())
        return my_list
    def value_mutation(self):
        """ 
        Function which is used to identify if a patient is new or old
        based on the patient_ID . 
  
        Parameters: NA  
        """
        if self.patient_id > 100:
            return "New Patient"
        else:
            return "Existing Patient"

