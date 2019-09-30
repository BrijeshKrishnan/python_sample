# importing libraries 
import time 
import math 

# decorator for logger 
# taken by any function. 

def my_logger(func):
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    file = open("automation.log","a") 
    file.write
    def inner1( *args, **kwargs): 
        file.write("*****************************\n")
        file.write("Enter func  "+func.__name__)
        # storing time before function execution 
        begin = time.time() 
        file.write ("\nStart time: %s"%begin)
        func(*args, **kwargs) 
        # storing time after function execution 
        end = time.time() 
        file.write ("\nEND time: %s"%end)
        file.write("\nExecution time : %s %s" %(func.__name__, end - begin)) 
        file.write("\n*****************************\n")
        file.close()
    return inner1 