# importing libraries 
import time 
import math 
# decorator for logger 
# taken by any function. 
def my_logger(func):
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    def inner1(*args, **kwargs): 
        print("******************")
        print("Enter func "+func.__name__)
        # storing time before function execution 
        begin = time.time() 
        print ("Start time: %s"%begin)
        func(*args, **kwargs) 
        # storing time after function execution 
        end = time.time() 
        print ("END time: %s"%end)
        print("Execution time : ", func.__name__, end - begin) 
    return inner1 