import os
import sys
sys.path.append(os.path.join((os.path.dirname(__file__))))
from src.patient import PatientClass

class TestSuperCool():
    """ 
    This is a class for testing the "simple_class" which is used for mutation
    testing example purpose. 
      
    Attributes: NA
    """
    def test_action(self):
        """ 
        The function test the PatientClass constructor and to get the 
        values which was initialised by the constructor. 
        Parameters: 
            NA
        Returns: 
            NA
        """
        pt = PatientClass("Dennis", 15000)
        assert pt.get_data() == ["Dennis", 15000]
    def test_action_1(self):
        """ 
        The function test the PatientClass constructor and to get the 
        values which was initialised by the constructor. 
        Parameters: 
            NA
        Returns: 
            NA
        """
        pt = PatientClass("Max", 15000)
        pt.change_data("Mark", 222)
        assert pt.get_data() == ["Mark", 222]
    def test_action_2(self):
        """ 
        The function test the PatientClass constructor and to get the 
        values which was initialized by the constructor and to test remove() function. 
        Parameters: 
            NA
        Returns: 
            NA
        """
        pt = PatientClass("Dennis", 15000)
        assert pt.get_data() == ["Dennis", 15000]
        pt.remove()
        assert pt.get_data() == [None, None]
    def test_action_3(self):
        """ 
        The function test the PatientClass constructor and to get the 
        values which was initialized by the constructor and to test value_mutation() function. 
        Parameters: 
            NA
        Returns: 
            NA
        """
        pt = PatientClass("Dennis", 15000)
        assert pt.get_data() == ["Dennis", 15000]
        assert pt.value_mutation() == "New Patient"

