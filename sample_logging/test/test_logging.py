import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.logging import my_logger

@my_logger
def test_file():
     for i in range (10):
         time.sleep(.5)
         print(i)
test_file()
